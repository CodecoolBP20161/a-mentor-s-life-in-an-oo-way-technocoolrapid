# Mentor

## Description
This class represents a mentor @ Codecool.

## Parent class
Person

## Attributes

* ```nick_name```
  * data type: String
  * description: stores a mentor nick name

* ```responsible```
  * data type: Boolean
  * description: stores whether a mentor is responsible for the week's project or not

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments
All of the arguments of the class itself and of the parent class except responsible.

#### Return value
None

### ```appoint_mentor```
Sets a value (Boolean) for the attribute responsible.
Printing the changes

#### Arguments
None

#### Return value
None

### ```create_by_csv```
Reads the data from the given database and fill it to a list

#### Arguments
* ```filename```
  * data type: String
  * description: stores a path and name of the database

#### Return value
list of Mentors
