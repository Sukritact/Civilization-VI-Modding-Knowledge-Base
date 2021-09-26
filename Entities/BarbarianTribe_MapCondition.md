---
tags:
- entity
- BarbarianTribe_MapCondition
- BarbarianTribe
- MapCondition
- Barbarian
- Tribe
- Map
- Condition
---
# BarbarianTribe_MapCondition
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.BarbarianTribe_MapCondition. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	MapConditionSetType	|	string	|		|		|		|	[[BarbarianTribe_MapConditionSet]].MapConditionSetType	|		|	|
|	TerrainType	|	string	|		|	✓	|		|	[[Terrain]].TerrainType	|		|	|
|	FeatureType	|	string	|		|	✓	|		|	[[Feature]].FeatureType	|		|	|
|	ResourceType	|	string	|		|	✓	|		|	[[Resource]].ResourceType	|		|	|
|	Range	|	number	|		|		|	0	|		|		|	|
|	Invert	|	boolean	|		|		|	0	|		|		|	|
|	MapConditionSetTypeReference	|	[[BarbarianTribe_MapConditionSet]]	|		|	✓	|		|		|		|	|
