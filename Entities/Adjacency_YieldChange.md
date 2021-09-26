---
tags:
- entity
- Adjacency_YieldChange
- Adjacency
- YieldChange
- Yield
- Change
---
# Adjacency_YieldChange
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Adjacency_YieldChange. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ID	|	string	|		|		|		|		|	✓	|	|
|	Description	|	string	|		|		|		|		|		|	|
|	YieldType	|	string	|		|		|		|	[[Yield]].YieldType	|		|	|
|	YieldChange	|	number	|		|		|	0	|		|		|	|
|	TilesRequired	|	number	|		|		|	1	|		|		|	|
|	OtherDistrictAdjacent	|	boolean	|		|		|	0	|		|		|	|
|	AdjacentSeaResource	|	boolean	|		|		|	0	|		|		|	|
|	AdjacentTerrain	|	string	|		|	✓	|		|	[[Terrain]].TerrainType	|		|	|
|	AdjacentFeature	|	string	|		|	✓	|		|	[[Feature]].FeatureType	|		|	|
|	AdjacentRiver	|	boolean	|		|		|	0	|		|		|	|
|	AdjacentWonder	|	boolean	|		|		|	0	|		|		|	|
|	AdjacentNaturalWonder	|	boolean	|		|		|	0	|		|		|	|
|	AdjacentImprovement	|	string	|		|	✓	|		|	[[Improvement]].ImprovementType	|		|	|
|	AdjacentDistrict	|	string	|		|	✓	|		|	[[District]].DistrictType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	ObsoleteCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	ObsoleteTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	AdjacentResource	|	boolean	|		|		|	0	|		|		|	|
|	AdjacentResourceClass	|	string	|		|		|	NO_RESOURCECLASS	|		|		|	|
|	Self	|	boolean	|		|		|	0	|		|		|	|
|	DistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	FeatureReference	|	[[Feature]]	|		|	✓	|		|		|		|	|
|	ImprovementReference	|	[[Improvement]]	|		|	✓	|		|		|		|	|
|	ObsoleteCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	ObsoleteTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	TerrainReference	|	[[Terrain]]	|		|	✓	|		|		|		|	|
|	YieldTypeReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
