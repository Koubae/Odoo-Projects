Views Map
---------

- Default Views
    
    - [Activity](#Activity)  
    - [Calendar](#Calendar)  
    - [Form](#Form)  
    - [Graph](#Graph) 
    - [Kanban](#Kanban) 
    - [List](#List)
    - [Pivot](#Pivot) 
    - [QWeb](#QWeb)
    - [Search](#Search)

- Enterprise's Views

    - [Cohort](#Cohort)
    - [Dashboard](#Dashboard) 
    - [Gantt](#Gantt) 
    - [Map](#Map)


-----------------------------------------------------------------------------------------------------

## Activity 


```

Activity 
        | - string
        | - name 
        | - templates
        | - widget
        | - record

```
-----------------------------------------------------------------------------------------------------

## Calendar


```

Calendar 
        | - date_start 
        | - date_stop 
        | - templates
        | - date_delay
        | - color
        | - form_view_id
        | - event_open_popup
        | - quick_add
        | - all_day
        | - mode
        | - scales
        | - <field>
                | - invisible 
                | - avatar_field 
                | - write_model & write_field
                | - filter & color 

```

-----------------------------------------------------------------------------------------------------

## Form

```

Form 
        | - <notebook>
                | - string  
                | - accesskey  
                | - attrs 
                | - filter & color 
        | - <group> 
        | - <sheet> 
        | - <header> 
        | - newline
        | - separator
        | - record
        # Semantic components
        | - <button>
            | - special  
            | - confirm  
        | - <field> 
            | - name   
            | - id  
            | - widget  
            | - options  
            | - <div class="">
                | - oe_inline  
                | - oe_left, oe_right  
                | - oe_read_only, oe_edit_only  
                | - oe_avatar  
            | - groups 
            | - on_change 
            | - attrs 
            | - domain 
            | - context 
            | - readonly 
            | - required 
            | - nolabel 
            | - placeholder 
            | - mode 
            | - help 
            | - filename 
            | - password 
            | - kanban_view_ref 
        | - <label> 
            | - for  
            | - string 

```

-----------------------------------------------------------------------------------------------------

## Graph

```

Graph 
        | - type 
        | - stacked 
        | - disable_linking
        | - order
        | - name 
        | - title 
        | - invisible 
        | - type
                | - row  
                | - col 
                | - measure
                | - interval

```

-----------------------------------------------------------------------------------------------------

## Kanban

```

Kanban 
        | - default_group_by 
        | - default_order 
        | - class
        | - examples
        | - group_create 
        | - group_delete 
        | - group_edit 
        | - quick_create
        | - quick_create_view
        | - records_draggable
        | - <field>
                | - name   
        | - <progressbar>
                | - field    
                | - colors  
                | - sum_field 
        | - <templates>
                | - widget    
                | - record  
                | - context  
                | - user_context  
                | - read_only_mode  
                | - selection_mode  

```


-----------------------------------------------------------------------------------------------------

## List

```

List 
        | - <tree>
            | - editable 
            | - multi_edit 
            | - default_order
            | - decoration-{$name}
            | - create, edit, delete, duplicate, import, export_xlsx
            | - limit 
            | - invisible 
            | - groups_limit
            | - expand
            | - <button>
                | - icon
                | - string
                | - object
                | - action
            | - name  
            | - args 
            | - attrs
            | - states
            | - field
            | - groupby
            | - control


```


-----------------------------------------------------------------------------------------------------


## Pivot

```

Pivot <pivot>
        | - disable_linking 
        | - display_quantity 
        | - default_order
        | - name 
        | - string 
        | - type     
                | - row  
                | - col 
                | - measure
                | - interval
                | - invisible

```


-----------------------------------------------------------------------------------------------------

## QWeb

```

QWeb name="arch"
        | - model 
        | - domain 
        | - context
        | - records 

```
-----------------------------------------------------------------------------------------------------


## Search

```

Search <search>
        | - name 
        | - string 
        | - operator
        | - filter_domain 
        | - context 
        | - groups     
        | - domain     
        | - filter     
                | - string   
                | - domain  
                | - date 
                | - default_period 
                | - context
                | - name
                | - help
                | - groups
        | - separator
        | - group
        | - searchpanel
                | - name  
                | - select  
                | - groups 
                | - string 
                | - icon 
                | - color 
                | - enable_counters 
                | - search_panel_select_range  
                | - expand 
                | - limit 

```

-----------------------------------------------------------------------------------------------------

# =============== < ENTERPRISE FEATURES > =============== #


## Cohort
```

Cohort   
        | - string
        | - date_start  
        | - date_stop 
        | - mode 
        | - timeline 
        | - interval  
        | - timeline 
        | - measure  
        | - <field>
                | - name  
                | - string  
                | - invisible  & write_field


```

-----------------------------------------------------------------------------------------------------

## Dashboard
```

Dashboard
        | - <view>
                | - type   
                | - ref    
                | - name    
        | - <group>
                | - string    
                | - colspan     
                | - col      
        | - <aggregate>
                | - field
                        | - integer   
                        | - float   
                        | - many2one     
                | - name     
                | - string      
                | - domain_label        
                | - group_operator         
                | - col         
                | - widget          
                | - help          
                | - measure           
                | - clickable           
                | - value_label  
                          
        | - <formula>
                | - value     
                | - name      
                | - string        
                | - col       
                | - widget        
                | - help        
                | - value_label         
        | - <widget>
                | - name      
                | - col  

```

-----------------------------------------------------------------------------------------------------

## Gantt
```

Gantt   
        | - date_start  
        | - date_stop 
        | - color 
        | - decoration-{$name}
                | - uid      
                | - today
                | - now
                | - {$name}
        | - default_group_by  
        | - consolidation 
        | - consolidation_max  
        | - consolidation_exclude
        | - create, cell_create, edit, delete, plan
                | - create  
                | - cell_create  
                | - edit
                | - edit
                | - plan
        | - offset
        | - progress
        | - string
        | - precision  
                | - hour  
                | - hour:half
                | - hour:quarter
                | - day
                | - day:half
                | - day
                | - edit
                | - day:half
                | - year 
        | - total_row 
        | - collapse_first_level 
        | - display_unavailability 
        | - default_scale 
                | - day  
                | - week
                | - month
                | - year
        | - scales 
        | - templates 
        | - widget 
        | - form_view_id 
        | - dynamic_range 
        | - thumbnails 

```

-----------------------------------------------------------------------------------------------------

## Map
```
Map <map>
        | - res_partner
        | - default_order  
        | - routing 
        | - hide_name 
        | - hide_address 
        | - name  
        | - string 
        | - measure  
        | - limit
```

-----------------------------------------------------------------------------------------------------