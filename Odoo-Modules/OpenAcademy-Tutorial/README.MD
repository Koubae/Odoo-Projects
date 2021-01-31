OpenAcademy Module 
=======================


Documentation
-------------

### Command line

```
# Start odoo
python odoo-bin -r [user_name] -w [password] --addons-path=addons -d [database_name]


# specifY Module directories
--addons-path

# Create a Odoo Module Project
odoo-bin scaffold [module_name] [module_position (Normally addons)]

# Update the Module 
odoo-bin -d [database_name] -u [module_name]

# Start Serer
python odoo-bin -d [database_name] -u [module_name] -r [user_name] -w [password]

python odoo-bin -r [user_name] -w [password] --addons-path=addons -d [database_name] -u [module_name]

```

### Composition of a module


**BUSINESS OBJECT | OBJECT VIEWS | DATA FILES | WEB CONTROLLERS | STATIC WEB DATA**

**Minimum Requirement**

```
module
    |
    |
    controllers
    demo
    models
    security
    views
    __init__.pypy
    __manifest.py
```

**Additional Elements**


```

module
    |
    |
    controllers
    data 
        | 
        |- data\files.xml ...
    demo
        |
        | -demo\fiels.xml ...
    i18n --> Translations
        |
        | - i18n\file.po ...
    models
        |
        | - models\file.py ...
    report
        |
        | - report\file.py ...
        | - report\file.xml (view) ...
    security
        |
        | - security\ir.model.access.csv
        | - security\file_group_security.xml
    static
        |
        | - src 
                |
                | - static\css
                | - static\img
                | - static\js
                | - static\scss
                | - static\xml
    tests 
        |
        | - tests\files.py ...        
    views
        |
        | -views\files.xml ...
    wizard
        |
        | - wizard\files.py ...
        | - wizard\files.xml ...
    __init__.pypy
    __manifest.py

```

-----------------------------------------------------------------------------------------------------

### Object-Relational Mapping | ORM 

Write SQL - Postgres statement as Python Syntax / OOP Classes.

- Model ORM
- Fields
- Attributes


#### Fields

**Reserved Fields**

These fields are managed by the system and shouldn’t be written to. They can be read if useful or necessary.

- id (Id)
    The unique identifier for a record in its model.
- create_date (Datetime)
    Creation date of the record.
- create_uid (Many2one)
    User who created the record.
- write_date (Datetime)
    Last modification date of the record.
- write_uid (Many2one)
    user who last modified the record.

-----------------------------------------------------------------------------------------------------

### Data Files

Data files have to be declasred in the manifest file to be loaded, they can be declared in the **'data'** list (always loaded) or in the **'demo'** list (only loaded in demonstration mode).


    <odoo>

            <record model="openacademy.course" id="course0">
                <field name="name">Course 0</field>
                <field name="description">Course 0's description

    Can have multiple lines
                </field>
            </record>
            <record model="openacademy.course" id="course1">
                <field name="name">Course 1</field>
                <!-- no description for this one -->
            </record>
            <record model="openacademy.course" id="course2">
                <field name="name">Course 2</field>
                <field name="description">Course 2's description</field>
            </record>

    </odoo>

* ```<record>```

    - **Attribute**

            model - > is the name of the Odoo model for the record.

            id -> is an external identifier, it allows referring to the record (without having to know its in-database identifier).

        
    - **Element**

        <field> - > Display Data to the View

            name=""  ->  the name of the field in the model 

-----------------------------------------------------------------------------------------------------

### Views


#### 1. Actions and Menus

Actions and menus are regular records in database, usually declared through data files. 

**The action must be declared before its corresponding menu in the XML file.**
**Data files are executed sequentially, the action’s id must be present in the database before the menu can be created.**


    <record model="ir.actions.act_window" id="action_list_ideas">
        <field name="name">Ideas</field>
        <field name="res_model">idea.idea</field>
        <field name="view_mode">tree,form</field>
    </record>
    <menuitem id="menu_ideas" parent="menu_root" name="Ideas" sequence="10"
            action="action_list_ideas"/>

* ```<record model="ir.actions.act_window" id="unique_id" >```


* ```<menuitem>```

    - **Attribute**

            id
            parent
            name
            action
            sequence

#### 2. Views

Views define the way the records of a model are displayed.
View inheritance allows altering views declared elsewhere (adding or removing content).
- [Odoo DOCS | View inheritance](https://www.odoo.com/documentation/14.0/reference/views.html#reference-views-inheritance).

**Views Types**

- Default Views
    
    - Activity | Calendar | Form | Graph | Kanban | List | Pivot | QWeb | Search

- Enterprise's Views

    - Cohort | Dashboard | Gantt | Map


For a major introspections of the Views types and attributes see --> [here]()

* ```<record model="ir.ui.view" id="unique_id" >```

**Generic view declaration**

    <record model="ir.ui.view" id="view_id">
        <field name="name">view.name</field>
        <field name="model">object_name</field>
        <field name="priority" eval="16"/>
        <field name="arch" type="xml">
            <!-- view content: <form>, <tree>, <graph>, ... -->
        </field>
    </record>

- **Views \ Fields \ name="" attr:**

- ```<<record id="MODEL_view_TYPE" model="ir.ui.view">
  <field name="[attr]">[value]</field>
    ```
    	- **Attribute**

            name --> Mandatory
            model --> Char  normally the custom Model Createad on the ORM
            priority (int)
            groups_id ---> Many2many odoo.addons.base.models.res_users.Groups
            arch  (text) The description of the view layout. + type="xml" or type="html"



-----------------------------------------------------------------------------------------------------

Credit and attribution
----------------------

This Module is the original OpenAcademy Tutorial, is included in my project as a reference but please refere to the original Tutorial / Guide.

### Odoo OpenAcademy | Building a Module

- [Building a Module](https://www.odoo.com/documentation/14.0/howtos/backend.html)

### Odoo | Technical training 
- [Technical training - Backend Development](https://www.odoo.com/fr_FR/slides/technical-training-backend-development-41)

-------------------------------------------------------

Odoo is a suite of business management software tools including CRM, e-commerce, billing, accounting, manufacturing, warehouse, project management, and inventory management and more.

### Odoo Main web Site:

- [Odoo](https://www.odoo.com)


### Odoo Source Code

- [Odoo | Source Code](https://github.com/odoo/odoo)




-----------------------------------------------------------------------------------------------------