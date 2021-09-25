---
tags:
- entity
- AiOperationDef
- Ai
- Operation
- Def
---
# AiOperationDef
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.AiOperationDef. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	OperationName	|	string	|		|		|		|		|	✓	|	|
|	TargetType	|	string	|		|		|		|	[[TargetType]].TargetType	|		|	|
|	TargetParameter	|	number	|		|		|	0	|		|		|	|
|	EnemyType	|	string	|		|		|	NONE	|		|		|	|
|	BehaviorTree	|	string	|		|	✓	|		|	[[BehaviorTree]].TreeName	|		|	|
|	Priority	|	number	|		|		|	3	|		|		|	|
|	MaxTargetDistInRegion	|	number	|		|		|	10	|		|		|	|
|	MaxTargetDistInArea	|	number	|		|		|	5	|		|		|	|
|	MaxTargetDistInWorld	|	number	|		|		|	0	|		|		|	|
|	MaxTargetStrength	|	number	|		|		|	-1	|		|		|	|
|	MaxTargetDefense	|	number	|		|		|	-1	|		|		|	|
|	MinOddsOfSuccess	|	number	|		|		|	0	|		|		|	|
|	SelfStart	|	boolean	|		|		|	0	|		|		|	|
|	MustBeAtWar	|	boolean	|		|		|	0	|		|		|	|
|	MustHaveNukes	|	boolean	|		|		|	0	|		|		|	|
|	MustHaveUnits	|	number	|		|		|	-1	|		|		|	|
|	OperationType	|	string	|		|	✓	|		|	[[AiOperationType]].OperationType	|		|	|
|	AllowTargetUpdate	|	boolean	|		|		|	1	|		|		|	|
|	TargetLuaScript	|	string	|		|	✓	|		|		|		|	|
|	ActiveEmergency	|	string	|		|	✓	|		|		|		|	|
