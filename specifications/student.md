# Student

## Description
This class represents a student @ Codecool.

## Parent class
Person

## Attributes

* ```late```
  * data type: Boolean
  * description: stores whether a student is late or not
* ```understood_project```
  * data type: Boolean
  * description: stores whether a student understood the project or not
  * default value: False

## Class methods

### ```create_by_csv```
Reads the data from the given database and fill it to a list

#### Arguments
* ```filename```
  * data type: String
  * description: stores a path and name of the database

#### Return value
list of Student

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments
All of the arguments of the class itself and of the parent class.

#### Return value
None

### ```understanding_project```
Sets a value (Boolean) for the attribute understood_project.
Update morale of the students depend he/she understands the project
Printing the changes

#### Arguments
variable called understood (Boolean)

#### Return value
None

### ```create_by_csv```
Reads the data from the given database and fill it to a list

#### Arguments
* ```filename```
  * data type: String
  * description: stores a path and name of the database

#### Return value
list of Student
