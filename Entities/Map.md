---
tags:
- entity
- Map
---
# Map
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Map. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	MapSizeType	|	string	|		|		|		|		|		|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	DefaultPlayers	|	number	|		|		|	0	|		|		|	|
|	FogTilesPerBarbarianCamp	|	number	|		|		|	0	|		|		|	|
|	NumNaturalWonders	|	number	|		|		|	0	|		|		|	|
|	UnitNameModifier	|	number	|		|		|	0	|		|		|	|
|	TargetNumCities	|	number	|		|		|	0	|		|		|	|
|	GridWidth	|	number	|		|		|	0	|		|		|	|
|	GridHeight	|	number	|		|		|	0	|		|		|	|
|	TerrainGrainChange	|	number	|		|		|	0	|		|		|	|
|	FeatureGrainChange	|	number	|		|		|	0	|		|		|	|
|	ResearchPercent	|	number	|		|		|	0	|		|		|	|
|	NumCitiesUnhealthPercent	|	number	|		|		|	0	|		|		|	|
|	NumCitiesPolicyCostMod	|	number	|		|		|	0	|		|		|	|
|	NumCitiesTechCostMod	|	number	|		|		|	0	|		|		|	|
|	EstimatedNumCities	|	number	|		|		|	0	|		|		|	|
|	PlateValue	|	number	|		|		|	4	|		|		|	|
|	Continents	|	number	|		|		|	1	|		|		|	|
|	GreatPersonClassesReference	|	[[Map_GreatPersonClass]]	|	✓	|	✓	|		|		|		|	|
