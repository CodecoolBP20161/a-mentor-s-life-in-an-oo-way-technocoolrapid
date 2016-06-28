# Event

## Description
This class represents an event @ Codecool, containing study and atmosphere related activities.

## Parent class
None

## Attributes

* ```name```
  * data type: string
  * description: stores the name of the activity/occurance taking place
* ```energy_level```
  * data type: integer
  * description: stores the energy level related to the activity/occurance (can be + or -)
* ```description```
  * data type: list of strings
  * description: stores the description for all events in the story

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments
All of the arguments of the class itself.

#### Return value
None

### ```have_coffee```
Checks energy_level of a person-object. If energy_level is below a certain level, person-object's
energy_level will be increased by an integer value.

#### Arguments
A variable called coffee_boost, with default value of integer.

#### Return value
None
