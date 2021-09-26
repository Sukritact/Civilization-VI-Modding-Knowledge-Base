---
tags:
- entity
- Feature
---
# Feature
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Feature. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	FeatureType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	Quote	|	string	|		|	✓	|		|		|		|	|
|	Coast	|	boolean	|		|		|	0	|		|		|	|
|	NoCoast	|	boolean	|		|		|	0	|		|		|	|
|	NoRiver	|	boolean	|		|		|	0	|		|		|	|
|	NoAdjacentFeatures	|	boolean	|		|		|	0	|		|		|	|
|	RequiresRiver	|	boolean	|		|		|	0	|		|		|	|
|	MovementChange	|	number	|		|		|	0	|		|		|	|
|	SightThroughModifier	|	number	|		|		|	0	|		|		|	|
|	Impassable	|	boolean	|		|		|	0	|		|		|	|
|	NaturalWonder	|	boolean	|		|		|	0	|		|		|	|
|	RemoveTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	Removable	|	boolean	|		|		|	0	|		|		|	|
|	AddCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	DefenseModifier	|	number	|		|		|	0	|		|		|	|
|	AddsFreshWater	|	boolean	|		|		|	0	|		|		|	|
|	Appeal	|	number	|		|		|	0	|		|		|	|
|	MinDistanceLand	|	number	|		|		|	0	|		|		|	|
|	MaxDistanceLand	|	number	|		|		|	0	|		|		|	|
|	NotNearFeature	|	boolean	|		|		|	0	|		|		|	|
|	Lake	|	boolean	|		|		|	0	|		|		|	|
|	Tiles	|	number	|		|		|	1	|		|		|	|
|	Adjacent	|	boolean	|		|		|	1	|		|		|	|
|	NoResource	|	boolean	|		|		|	0	|		|		|	|
|	DoubleAdjacentTerrainYield	|	boolean	|		|		|	0	|		|		|	|
|	NotCliff	|	boolean	|		|		|	0	|		|		|	|
|	MinDistanceNW	|	number	|		|		|	-1	|		|		|	|
|	CustomPlacement	|	string	|		|	✓	|		|		|		|	|
|	Forest	|	boolean	|		|		|	0	|		|		|	|
|	AntiquityPriority	|	number	|		|		|	0	|		|		|	|
|	QuoteAudio	|	string	|		|	✓	|		|		|		|	|
|	Settlement	|	boolean	|		|		|	1	|		|		|	|
|	FollowRulesInWB	|	boolean	|		|		|	1	|		|		|	|
|	DangerValue	|	number	|		|		|	0	|		|		|	|
|	AddCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	AdjacentFeatures	|	[[Feature]]	|	✓	|	✓	|		|		|		|	|
|	AdjacentTerrains	|	[[Terrain]]	|	✓	|	✓	|		|		|		|	|
|	AdjacentYields	|	[[Feature_AdjacentYield]]	|	✓	|	✓	|		|		|		|	|
|	FeatureRemoveCollection	|	[[Feature_Remove]]	|	✓	|	✓	|		|		|		|	|
|	NotAdjacentTerrains	|	[[Terrain]]	|	✓	|	✓	|		|		|		|	|
|	NotNearFeatures	|	[[Feature]]	|	✓	|	✓	|		|		|		|	|
|	RemoveTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	StartBiasFeatureCollection	|	[[StartBiasFeature]]	|	✓	|	✓	|		|		|		|	|
|	UnitMovements	|	[[Feature_UnitMovement]]	|	✓	|	✓	|		|		|		|	|
|	ValidTerrains	|	[[Terrain]]	|	✓	|	✓	|		|		|		|	|
|	YieldChanges	|	[[Feature_YieldChange]]	|	✓	|	✓	|		|		|		|	|
