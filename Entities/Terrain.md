---
tags:
- entity
- Terrain
---
# Terrain
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Terrain. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TerrainType	|	string	|		|		|		|		|		|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Mountain	|	boolean	|		|		|	0	|		|		|	|
|	Hills	|	boolean	|		|		|	0	|		|		|	|
|	Water	|	boolean	|		|		|	0	|		|		|	|
|	InfluenceCost	|	number	|		|		|		|		|		|	|
|	MovementCost	|	number	|		|		|		|		|		|	|
|	ShallowWater	|	boolean	|		|		|	0	|		|		|	|
|	SightModifier	|	number	|		|		|	0	|		|		|	|
|	SightThroughModifier	|	number	|		|		|	0	|		|		|	|
|	Impassable	|	boolean	|		|		|	0	|		|		|	|
|	DefenseModifier	|	number	|		|		|	0	|		|		|	|
|	Appeal	|	number	|		|		|	0	|		|		|	|
|	AntiquityPriority	|	number	|		|		|	0	|		|		|	|
|	ImprovementAdjacentTerrainCollection	|	[[Improvement_ValidAdjacentTerrain]]	|	✓	|	✓	|		|		|		|	|
|	ImprovementCollection	|	[[Improvement_ValidTerrain]]	|	✓	|	✓	|		|		|		|	|
|	StartBiasTerrainCollection	|	[[StartBiasTerrain]]	|	✓	|	✓	|		|		|		|	|
|	TerrainClasses	|	[[TerrainClass]]	|	✓	|	✓	|		|		|		|	|
|	ValidResources	|	[[Resource]]	|	✓	|	✓	|		|		|		|	|
