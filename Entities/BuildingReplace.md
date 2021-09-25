---
tags:
- entity
- BuildingReplace
- Building
- Replace
---
# BuildingReplace
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.BuildingReplace. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	CivUniqueBuildingType	|	string	|		|		|		|	[[Building]].BuildingType	|		|	|
|	ReplacesBuildingType	|	string	|		|		|		|	[[Building]].BuildingType	|		|	|
|	BaseBuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	ReplacementBuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
