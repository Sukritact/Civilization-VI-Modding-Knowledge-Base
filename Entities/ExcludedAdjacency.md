---
tags:
- entity
- ExcludedAdjacency
- Excluded
- Adjacency
---
# ExcludedAdjacency
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.ExcludedAdjacency. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TraitType	|	string	|		|		|		|	[[Trait]].TraitType	|		|	|
|	YieldChangeId	|	string	|		|		|		|	[[Adjacency_YieldChange]].ID	|		|	|
|	TraitReference	|	[[Trait]]	|		|	✓	|		|		|		|	|
