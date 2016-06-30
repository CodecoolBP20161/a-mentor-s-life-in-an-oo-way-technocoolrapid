# AssignmentClass

## Description
This class represents an assignment @ Codecool, containing assignments the students and mentors have to work on.

## Parent class
None

## Attributes

* ```name```
  * data type: string
  * description: stores the name of the assignment
* ```difficulty```
    * data type: integer
    * description: stores the difficulty of the assignment
* ```grade```
  * default value: None
  * data type: integer
  * description: stores the grade the student got for his/her assignment
* ```is_active```
  * data type: boolean
  * description: stores whether the assignment is a current or a past one
* ```student```
  * data type: containing Student object
  * description: stores the student who's working on this assignment
* ```mentor```
  * data type: containing mentor object
  * description: stores the mentor who'll grade this assignment
* ```questions```
 * data type: list of strings
 * description: stores questions about the assignment (for understanding)



## Instance methods

### ``` __init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ``` get_grade```

Gives back a pretty printed version of the ```student's```name, the assignment he/she's working on and the grade

#### Arguments
* self


#### Return value
list of moral of mentor (integer) and reaction(string)



### ```understand_assignment```

#### Arguments
* ```student```
  * data_type: Student object
  * description: holds the name of the student in question

#### Return value
Boolean value(True/False)
