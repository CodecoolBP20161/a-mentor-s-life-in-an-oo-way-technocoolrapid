# Athomosphere

## Description
This class contains events with impact on the ```morale``` attribute of ```Person``` objects.

## Parent classes
* ```Event```

## Attributes
* ```moral_change```
    * data type: integer
    * description: the moral of a person changes this much if the event takes place
* ```moral_message```
    * data type: string
    * description: this message is given as feedback when the event takes place
* ```_id``` class attribute
    * data type: string
    * descrition: specifies that the moral value has to be changed

## Class methods

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments
* all attributes

#### Return value
* ```None```

### ```process_atmosphere```

#### Arguments
* none

#### Return value
list: moral_change, moral_message, _id
