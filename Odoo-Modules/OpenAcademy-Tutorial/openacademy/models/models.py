from odoo import models, fields, api, exceptions, _
from datetime import timedelta

Model = models.Model

class Course(Model):

    _name = 'openacademy.course'
    _description = 'OpenAcademy Courses'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users', 
                                    ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")


    def copy(self, default=None):
        """
        Re-implemented method which allows to duplicate the Course object, changing the original name into “Copy of [original name]”. Then Calls the Inherited copy again.

        Original Copy is in self --> Model --> AbstractModel --> BaseModel
        """

        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', _(f'Copy of {self.name}%'))]
        )

        if not copied_count:
            new_name = _(f'Copy of {self.name}')
        else:
            new_name = _(f"Copy of {self.name} ({copied_count})")
        
        default['name'] = new_name
        return super().copy(default)

    
    _sql_constraints = [
        ('name_description_check', 'CHECK(name != description)', 
        "The title of the course should not be the description"),

        ('name_unique', 'UNIQUE(name)', 
        "The course title must be unique"),
    ]


class Session(Model):

    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    color = fields.Integer()

    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=['|', ('instructor', '=', True),
                ('category_id.name', 'ilike', "Teacher")])
    
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', 
                                string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    # ---- Computed Field
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats', default="50")
    end_date = fields.Date(string="End Date", store=True, compute='_get_end_date', inverse='_set_end_date')
    attendees_count = fields.Integer(string="Attendees count", compute='_get_attendees_count', store=True)

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for item in self:
            if not item.seats:
                item.taken_seats = 0.0
            else:
                item.taken_seats = 100.0 * len(item.attendee_ids) / item.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': _("Incorrect 'seats' value"),
                    'message': _("The number of available seats may not be negative"),
                },
            }
        
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': _("Too many attendees"),
                    'message': _("Increase seats or remove excess attendees"),
                },
            }

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for item in self:
            if not (item.start_date and item.duration):
                item.end_date = item.start_date
                continue
            else:
                # NOTE: Add duration to start_date, but: Monday + 5 days = Saturday, so
                # subtract one second to get on Friday instead
                duration = timedelta(days=item.duration, seconds= -1)
                item.end_date = item.start_date + duration
    
    def _set_end_date(self):
        for item in self:
            if not (item.start_date and item.end_date):
                continue
                
            # NOTE: Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            item.duration = (item.end_date - item.start_date).days + 1
        
    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for item in self:
            item.attendees_count = len(item.attendee_ids)

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for item in self:
            if item.instructor_id and item.instructor_id in item.attendee_ids:
                raise exceptions.ValidationError(_("A session's instructor can't be an attendee"))



