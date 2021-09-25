---
tags:
- entity
- BarbarianAttackForce
- Barbarian
- Attack
- Force
---
# BarbarianAttackForce
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.BarbarianAttackForce. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	AttackForceType	|	string	|		|		|		|		|	✓	|	|
|	MinTargetDifficulty	|	string	|		|	✓	|		|	[[Difficulty]].DifficultyType	|		|	|
|	MaxTargetDifficulty	|	string	|		|	✓	|		|	[[Difficulty]].DifficultyType	|		|	|
|	SpawnRate	|	number	|		|		|	2	|		|		|	|
|	MeleeTag	|	string	|		|	✓	|		|		|		|	|
|	NumMeleeUnits	|	number	|		|		|	0	|		|		|	|
|	RangeTag	|	string	|		|	✓	|		|		|		|	|
|	NumRangeUnits	|	number	|		|		|	0	|		|		|	|
|	SiegeTag	|	string	|		|	✓	|		|		|		|	|
|	NumSiegeUnits	|	number	|		|		|	0	|		|		|	|
|	SupportTag	|	string	|		|	✓	|		|		|		|	|
|	NumSupportUnits	|	number	|		|		|	0	|		|		|	|
|	RaidingForce	|	boolean	|		|		|	0	|		|		|	|
|	MaxDifficultyReference	|	[[Difficulty]]	|		|	✓	|		|		|		|	|
|	MinDifficultyReference	|	[[Difficulty]]	|		|	✓	|		|		|		|	|
