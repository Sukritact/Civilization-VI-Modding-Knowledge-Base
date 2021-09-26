---
tags:
- entity
- NamedLakeCivilization
- XP2
- Named
- Lake
- Civilization
---
# NamedLakeCivilization
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.NamedLakeCivilization. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	NamedLakeType	|	string	|		|		|		|	[[NamedLake]].NamedLakeType	|		|	|
|	CivilizationType	|	string	|		|		|		|	[[Civilization]].CivilizationType	|		|	|
|	NamedLakeReference	|	[[NamedLake]]	|		|	✓	|		|		|		|	|
