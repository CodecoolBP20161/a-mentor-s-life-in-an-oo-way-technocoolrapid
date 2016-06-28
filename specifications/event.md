# Event

## Description
This class represents an event @ Codecool, containing study and atmosphere related activities.

## Parent class
None

## Attributes

* ```energy_level```
  * data type: integer
  * description: stores the energy level related to the activity/occurrence (can be + or -)
* ```description```
  * data type: string
  * description: stores the description for the event
* ```event_id``` class attribute
  * data type: string
  * description: specifies that the energy_level value has to be changed

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments
All of the arguments of the class itself.

#### Return value
None

### ```process_event```
Returns the energy_level, description and event_id of the event.

#### Arguments
None

#### Return value
List: energy_level, description, event_id
