---
tags:
- entity
- Building_GreatPersonPoint
- Building
- GreatPersonPoint
- Great
- Person
- Point
---
# Building_GreatPersonPoint
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Building_GreatPersonPoint. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	BuildingType	|	string	|		|		|		|	[[Building]].BuildingType	|		|	|
|	GreatPersonClassType	|	string	|		|		|		|	[[GreatPersonClass]].GreatPersonClassType	|		|	|
|	PointsPerTurn	|	number	|		|		|	0	|		|		|	|
|	BuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	GreatPersonClassReference	|	[[GreatPersonClass]]	|		|	✓	|		|		|		|	|
