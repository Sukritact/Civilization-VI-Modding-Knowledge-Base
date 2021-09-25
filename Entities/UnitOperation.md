---
tags:
- entity
- UnitOperation
- Unit
- Operation
---
# UnitOperation
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.UnitOperation. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	OperationType	|	string	|		|		|		|		|	✓	|	|
|	Description	|	string	|		|		|		|		|		|	|
|	Help	|	string	|		|	✓	|		|		|		|	|
|	DisabledHelp	|	string	|		|	✓	|		|		|		|	|
|	Icon	|	string	|		|		|		|		|		|	|
|	Sound	|	string	|		|	✓	|		|		|		|	|
|	VisibleInUI	|	boolean	|		|		|		|		|		|	|
|	HoldCycling	|	boolean	|		|		|	0	|		|		|	|
|	CategoryInUI	|	string	|		|	✓	|		|		|		|	|
|	InterfaceMode	|	string	|		|	✓	|		|		|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	Turns	|	number	|		|		|	0	|		|		|	|
|	BaseProbability	|	number	|		|		|	0	|		|		|	|
|	LevelProbChange	|	number	|		|		|	0	|		|		|	|
|	EnemyProbChange	|	number	|		|		|	0	|		|		|	|
|	EnemyLevelProbChange	|	number	|		|		|	0	|		|		|	|
|	TargetDistrict	|	string	|		|	✓	|		|	[[District]].DistrictType	|		|	|
|	HotkeyId	|	string	|		|	✓	|		|		|		|	|
|	Offensive	|	boolean	|		|		|	0	|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	TargetDistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
