---
tags:
- entity
- BarbarianTribeName
- Barbarian
- Tribe
- Name
---
# BarbarianTribeName
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.BarbarianTribeName. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TribeNameType	|	string	|		|		|		|		|	✓	|	|
|	TribeType	|	string	|		|		|		|	[[BarbarianTribe]].TribeType	|		|	|
|	NumMilitary	|	number	|		|	✓	|	5	|		|		|	|
|	NumScouts	|	number	|		|	✓	|		|		|		|	|
|	PercentRangedUnits	|	number	|		|	✓	|		|		|		|	|
|	TurnsToWarriorSpawn	|	number	|		|	✓	|		|		|		|	|
|	TribeDisplayName	|	string	|		|		|		|		|		|	|
|	ScoutingBehaviorTree	|	string	|		|	✓	|		|		|		|	|
|	RaidingBehaviorTree	|	string	|		|	✓	|		|		|		|	|
|	RaidingBoldness	|	number	|		|	✓	|		|		|		|	|
|	AttackCollection	|	[[BarbarianAttackForce]]	|	✓	|	✓	|		|		|		|	|
|	TribeTypeReference	|	[[BarbarianTribe]]	|		|	✓	|		|		|		|	|
