---
tags:
- entity
- BuildingPrereq
- Building
- Prereq
---
# BuildingPrereq
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.BuildingPrereq. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Building	|	string	|		|		|		|	[[Building]].BuildingType	|		|	|
|	PrereqBuilding	|	string	|		|		|		|	[[Building]].BuildingType	|		|	|
|	BuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	PrereqBuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
