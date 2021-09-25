---
tags:
- entity
- DistrictReplace
- District
- Replace
---
# DistrictReplace
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.DistrictReplace. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	CivUniqueDistrictType	|	string	|		|		|		|	[[District]].DistrictType	|	✓	|	|
|	ReplacesDistrictType	|	string	|		|		|		|	[[District]].DistrictType	|		|	|
|	BaseDistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	ReplacementDistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|