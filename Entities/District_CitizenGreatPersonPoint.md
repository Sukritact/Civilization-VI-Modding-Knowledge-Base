---
tags:
- entity
- District_CitizenGreatPersonPoint
- District
- CitizenGreatPersonPoint
- Citizen
- Great
- Person
- Point
---
# District_CitizenGreatPersonPoint
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.District_CitizenGreatPersonPoint. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	DistrictType	|	string	|		|		|		|	[[District]].DistrictType	|		|	|
|	GreatPersonClassType	|	string	|		|		|		|	[[GreatPersonClass]].GreatPersonClassType	|		|	|
|	PointsPerTurn	|	number	|		|		|	0	|		|		|	|
|	DistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	GreatPersonClassReference	|	[[GreatPersonClass]]	|		|	✓	|		|		|		|	|
