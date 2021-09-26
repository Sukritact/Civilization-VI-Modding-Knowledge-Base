---
tags:
- entity
- BonusMinorStartingUnit
- Bonus
- Minor
- Starting
- Unit
---
# BonusMinorStartingUnit
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.BonusMinorStartingUnit. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Unit	|	string	|		|		|		|	[[Unit]].UnitType	|		|	|
|	Era	|	string	|		|		|		|	[[Era]].EraType	|		|	|
|	Quantity	|	number	|		|		|	1	|		|		|	|
|	OnDistrictCreated	|	boolean	|		|		|	0	|		|		|	|
|	District	|	string	|		|		|	DISTRICT_CITY_CENTER	|		|		|	|
|	MinDifficulty	|	string	|		|	✓	|		|	[[Difficulty]].DifficultyType	|		|	|
|	DifficultyDelta	|	number	|		|		|	0	|		|		|	|
|	DifficultyReference	|	[[Difficulty]]	|		|	✓	|		|		|		|	|
|	EraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	UnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
