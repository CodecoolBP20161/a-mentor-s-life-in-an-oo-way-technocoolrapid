# Study Class

## Description
This class represents a study evenets in Codecool, containing energy level and  skill level modifier events.

## Parent class
Event

## Attributes

* ```skill_level```
  * data type: int
  * description: represents the event's skill level modifier affect

* ```describe_study```
  * data type: string
  * description: represents the event's skill level modifier affect in text


## Class methods

none

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the study itself plus parent class arguments .

#### Return value
```describe```

### ```process_study```


#### Arguments

#### Return value
list of [skill_level, describe, "skill_level"]
