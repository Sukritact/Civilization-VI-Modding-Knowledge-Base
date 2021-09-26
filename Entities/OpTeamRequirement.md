---
tags:
- entity
- OpTeamRequirement
- Op
- Team
- Requirement
---
# OpTeamRequirement
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.OpTeamRequirement. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TeamName	|	string	|		|		|		|	[[AiTeam]].TeamName	|		|	|
|	AiType	|	string	|		|		|		|	[[UnitAiType]].AiType	|		|	|
|	MinNumber	|	number	|		|	✓	|		|		|		|	|
|	MaxNumber	|	number	|		|	✓	|		|		|		|	|
|	MinPercentage	|	number	|		|		|	0	|		|		|	|
|	MaxPercentage	|	number	|		|		|	1	|		|		|	|
|	ReconsiderWhilePreparing	|	boolean	|		|		|	0	|		|		|	|
|	AiTypeDependence	|	string	|		|	✓	|		|	[[UnitAiType]].AiType	|		|	|
|	AiTypeDependenceReference	|	[[UnitAiType]]	|		|	✓	|		|		|		|	|
