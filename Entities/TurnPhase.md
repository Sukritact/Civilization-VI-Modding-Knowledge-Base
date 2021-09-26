---
tags:
- entity
- TurnPhase
- Turn
- Phase
---
# TurnPhase
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.TurnPhase. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ID	|	number	|		|	✓	|		|		|	✓	|	|
|	TurnPhaseType	|	string	|		|		|		|		|		|	|
|	PhaseOrder	|	number	|		|		|		|		|		|	|
|	TurnMode	|	string	|		|		|		|		|		|	|
|	ActiveSegmentType	|	string	|		|		|		|	[[TurnSegment]].TurnSegmentType	|		|	|
|	InactiveSegmentType	|	string	|		|	✓	|		|	[[TurnSegment]].TurnSegmentType	|		|	|
|	ActiveSegment	|	[[TurnSegment]]	|		|	✓	|		|		|		|	|
|	InactiveSegment	|	[[TurnSegment]]	|		|	✓	|		|		|		|	|
