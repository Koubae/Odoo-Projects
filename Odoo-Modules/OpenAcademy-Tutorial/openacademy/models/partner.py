from odoo import fields, models

class Partner(models.Model):
    """
    Add a new column to the res.partner model, by default partners are not
    instructors
    """
    _inherit = 'res.partner'
    print('==='*15)
   
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('openacademy.session',
        string="Attended Sessions", readonly=True)