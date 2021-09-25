---
tags:
- entity
- MajorStartingUnit
- Major
- Starting
- Unit
---
# MajorStartingUnit
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.MajorStartingUnit. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Unit	|	string	|		|		|		|	[[Unit]].UnitType	|		|	|
|	Era	|	string	|		|		|		|	[[Era]].EraType	|		|	|
|	District	|	string	|		|		|	DISTRICT_CITY_CENTER	|	[[District]].DistrictType	|		|	|
|	Quantity	|	number	|		|		|	1	|		|		|	|
|	NotStartTile	|	boolean	|		|		|	0	|		|		|	|
|	OnDistrictCreated	|	boolean	|		|		|	0	|		|		|	|
|	AiOnly	|	boolean	|		|		|	0	|		|		|	|
|	MinDifficulty	|	string	|		|	✓	|		|	[[Difficulty]].DifficultyType	|		|	|
|	DifficultyDelta	|	number	|		|		|	0	|		|		|	|
|	DifficultyReference	|	[[Difficulty]]	|		|	✓	|		|		|		|	|
|	EraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	UnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
