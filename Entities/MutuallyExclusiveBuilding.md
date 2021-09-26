---
tags:
- entity
- MutuallyExclusiveBuilding
- Mutually
- Exclusive
- Building
---
# MutuallyExclusiveBuilding
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.MutuallyExclusiveBuilding. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Building	|	string	|		|		|		|	[[Building]].BuildingType	|		|	|
|	MutuallyExclusiveBuilding	|	string	|		|		|		|	[[Building]].BuildingType	|		|	|
|	BuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	MutuallyExclusiveBuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
