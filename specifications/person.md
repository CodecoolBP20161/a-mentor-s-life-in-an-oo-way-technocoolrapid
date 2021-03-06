# Person

## Description
This class represents a person parent class, containing the persons attributes and methods.

## Parent class
None

## Attributes
first_name: string, last_name: string, year_of_birth: integer, gender: string
* ```first_name```
  * data type: string
  * description: stores the person's first name
* ```last_name```
  * data type: string
  * description: stores the person's last name
* ```year_of_birth```
   * data type: integer
   * description: stores the person's year of birth
* ```gender```
  * data type: string
  * description: stores the persons genre: (female, male, notsure)
* ```energy_level```
     * data type: integer
     * description: stores the person's actual energy level
* ```skill_level```
    * data type: integer
    * description: stores the person's actual skill level
* ```moral_level```
    * data type: integer
    * description: stores the person's actual moral level
* ```hungry```
    * data type: bool
    * description: stores the person's hungry state
* ```last_name_list```
    * data type: list
    * description: stores the person's last names
* ```female_name_list```
    * data type: list
    * description: stores the female's name
* ```male_name_list```
    * data type: list
    * description: stores the male's name

## Class methods


## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

first_name, last_name, year_of_birth, gender, energy_level, moral_level, skill_level, hungry

#### Return value
None

### ```process```

Updates Person attributes and printing the changes
#### Arguments
* ```event_list```
  * data_type: list [int, string, string]
  * description: holds the attributes of event_list

#### Return value
None

### ```get_full_name```

Person's full name by first and last name
#### Arguments

#### Return value
string
