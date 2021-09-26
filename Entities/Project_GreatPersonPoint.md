---
tags:
- entity
- Project_GreatPersonPoint
- Project
- GreatPersonPoint
- Great
- Person
- Point
---
# Project_GreatPersonPoint
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Project_GreatPersonPoint. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ProjectType	|	string	|		|		|		|	[[Project]].ProjectType	|		|	|
|	GreatPersonClassType	|	string	|		|		|		|	[[GreatPersonClass]].GreatPersonClassType	|		|	|
|	Points	|	number	|		|		|	0	|		|		|	|
|	PointProgressionModel	|	string	|		|		|	NO_PROGRESSION_MODEL	|		|		|	|
|	PointProgressionParam1	|	number	|		|		|	0	|		|		|	|
|	GreatPersonClassReference	|	[[GreatPersonClass]]	|		|	✓	|		|		|		|	|
|	ProjectReference	|	[[Project]]	|		|	✓	|		|		|		|	|
