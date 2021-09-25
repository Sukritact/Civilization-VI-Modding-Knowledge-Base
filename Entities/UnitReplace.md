---
tags:
- entity
- UnitReplace
- Unit
- Replace
---
# UnitReplace
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.UnitReplace. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	CivUniqueUnitType	|	string	|		|		|		|	[[Unit]].UnitType	|	✓	|	|
|	ReplacesUnitType	|	string	|		|		|		|	[[Unit]].UnitType	|		|	|
|	BaseUnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
|	ReplacementUnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
