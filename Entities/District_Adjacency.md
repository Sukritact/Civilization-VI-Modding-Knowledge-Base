---
tags:
- entity
- District_Adjacency
- District
- Adjacency
---
# District_Adjacency
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.District_Adjacency. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	DistrictType	|	string	|		|		|		|	[[District]].DistrictType	|		|	|
|	YieldChangeId	|	string	|		|		|		|	[[Adjacency_YieldChange]].ID	|		|	|
|	YieldChangeReference	|	[[Adjacency_YieldChange]]	|		|	✓	|		|		|		|	|
