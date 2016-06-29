# CodecoolClass

## Description
This class represents a real class @ Codecool, containing mentors and students working at the class.

## Parent class
None

## Attributes

* ```location```
  * data type: string
  * description: stores the city where the the class started
* ```year```
  * data type: integer
  * description: stores the year when the class started
* ```mentors```
   * data type: list (containing Mentor objects)
   * description: stores the mentors of the class
* ```students```
  * data type: list (containing Student objects)
  * description: stores the students of the class
* ```stat_morning```
  * data type: integer
  * description: stores the morning's energy, moral and skill level of the class
* ```stat_evening```
  * data type: integer
  * description: stores the evening's energy, moral and skill level of the class  

## Class methods

### ```generate_local```

Creates a ```CodecoolClass``` object having some real-life data from the implementer students' real class.

#### Arguments
None

#### Return value

```CodecoolClass``` object

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```find_student_by_full_name```

Gives back a student with the same full name as the argument from ```students```
#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the student to be found

#### Return value
```Student``` object

### ```find_mentor_by_full_name```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the mentor to be found

#### Return value
```Mentor``` object

### ```appoint_mentor```
Select random mentor from the mentors list
and call for its appoint_mentor method

#### Arguments
None

#### Return value
None


### ```export_to_csv```
write to file

#### Arguments
* ```file_name```
  * data_type: string
  * description: csv database file name


#### Return value
list of lists

### ```sum_stats```
Summing the class moral, energy level and skill level before and after school

#### Arguments
* ```stat_status```
  * data_type: string
  * description: where to store the statistic data


#### Return value
integer

### ```report_day```
Prints the state changes between start and end of the school.

#### Arguments
* ```stat_morning```
  * data_type: integer
  * description: statistic before the school

* ```stat_evening```
  * data_type: integer
  * description: statistic after the school

#### Return value
None

### ```attendance_check```
Checks the students if they are late and modifies the mentor's morale

#### Arguments
None

#### Return value
list of integer, string, string
