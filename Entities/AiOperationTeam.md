---
tags:
- entity
- AiOperationTeam
- Ai
- Operation
- Team
---
# AiOperationTeam
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.AiOperationTeam. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TeamName	|	string	|		|		|		|	[[AiTeam]].TeamName	|		|	|
|	OperationName	|	string	|		|		|		|	[[AiOperationDef]].OperationName	|		|	|
|	MinUnits	|	number	|		|		|	1	|		|		|	|
|	MaxUnits	|	number	|		|		|	-1	|		|		|	|
|	InitialStrengthAdvantage	|	number	|		|		|	0	|		|		|	|
|	OngoingStrengthAdvantage	|	number	|		|		|	0	|		|		|	|
|	SafeRallyPoint	|	boolean	|		|		|	0	|		|		|	|
|	Condition	|	string	|		|	✓	|		|		|		|	|
