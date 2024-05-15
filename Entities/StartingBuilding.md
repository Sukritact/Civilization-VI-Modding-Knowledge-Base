---
tags:
- entity
- StartingBuilding
- Starting
- Building
---
# StartingBuilding
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.StartingBuilding. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Building	|	string	|		|		|		|	[[Building]].BuildingType	|		|	|
|	Era	|	string	|		|		|		|	[[Era]].EraType	|		|	|
|	District	|	string	|		|	✓	|		|	[[District]].DistrictType	|		|	|
|	MinorOnly	|	boolean	|		|		|	0	|		|		|	|
|	MinDifficulty	|	string	|		|	✓	|		|	[[Difficulty]].DifficultyType	|		|	|
|	BuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	DifficultyReference	|	[[Difficulty]]	|		|	✓	|		|		|		|	|
|	DistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	EraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
