---
tags:
- entity
- Unit_BuildingPrereq
- Unit
- BuildingPrereq
- Building
- Prereq
---
# Unit_BuildingPrereq
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Unit_BuildingPrereq. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Unit	|	string	|		|		|		|	[[Unit]].UnitType	|		|	|
|	PrereqBuilding	|	string	|		|		|		|	[[Building]].BuildingType	|		|	|
|	NumSupported	|	number	|		|		|	-1	|		|		|	|
|	PrereqBuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	UnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
