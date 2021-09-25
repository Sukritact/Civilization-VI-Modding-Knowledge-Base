---
tags:
- entity
- TurnSegment
- Turn
- Segment
---
# TurnSegment
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.TurnSegment. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TurnSegmentType	|	string	|		|		|		|		|		|	|
|	Name	|	string	|		|	✓	|		|		|		|	|
|	Sound	|	string	|		|	✓	|		|		|		|	|
|	AllowStrategicCommands	|	boolean	|		|		|	0	|		|		|	|
|	AllowTacticalCommands	|	boolean	|		|		|	0	|		|		|	|
|	TimeLimit_Base	|	number	|		|		|	0	|		|		|	|
|	TimeLimit_PerCity	|	number	|		|		|	0	|		|		|	|
|	TimeLimit_PerUnit	|	number	|		|		|	0	|		|		|	|
|	AllowTurnUnready	|	boolean	|		|		|	1	|		|		|	|
