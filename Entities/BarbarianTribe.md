---
tags:
- entity
- BarbarianTribe
- Barbarian
- Tribe
---
# BarbarianTribe
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.BarbarianTribe. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TribeType	|	string	|		|		|		|		|	✓	|	|
|	IsCoastal	|	boolean	|		|		|	0	|		|		|	|
|	RequiredResource	|	string	|		|	✓	|		|	[[Resource]].ResourceType	|		|	|
|	ResourceRange	|	number	|		|		|	0	|		|		|	|
|	PercentRangedUnits	|	number	|		|		|	0	|		|		|	|
|	TurnsToWarriorSpawn	|	number	|		|		|	15	|		|		|	|
|	ScoutTag	|	string	|		|		|		|		|		|	|
|	MeleeTag	|	string	|		|		|		|		|		|	|
|	RangedTag	|	string	|		|		|		|		|		|	|
|	SiegeTag	|	string	|		|		|		|		|		|	|
|	DefenderTag	|	string	|		|		|		|		|		|	|
|	SupportTag	|	string	|		|	✓	|		|		|		|	|
|	ScoutingBehaviorTree	|	string	|		|		|		|		|		|	|
|	RaidingBehaviorTree	|	string	|		|		|		|		|		|	|
|	RaidingBoldness	|	number	|		|		|	20	|		|		|	|
|	CityAttackOperation	|	string	|		|		|		|		|		|	|
|	CityAttackBoldness	|	number	|		|		|	25	|		|		|	|
|	Name	|	string	|		|	✓	|		|		|		|	|
|	AttackCollection	|	[[BarbarianAttackForce]]	|	✓	|	✓	|		|		|		|	|
|	RequiredResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
|	TribeNames	|	[[BarbarianTribeName]]	|	✓	|	✓	|		|		|		|	|
