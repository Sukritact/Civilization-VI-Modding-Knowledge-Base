---
tags:
- entity
- Yield
---
# Yield
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Yield. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	YieldType	|	string	|		|		|		|		|		|	|
|	Name	|	string	|		|		|		|		|		|	|
|	IconString	|	string	|		|		|		|		|		|	|
|	OccupiedCityChange	|	number	|		|		|	0	|		|		|	|
|	DefaultValue	|	number	|		|		|	1	|		|		|	|
|	FeatureChange_Refs	|	[[Feature_YieldChange]]	|	✓	|	✓	|		|		|		|	|
|	ImprovementChange_Refs	|	[[Improvement_BonusYieldChange]]	|	✓	|	✓	|		|		|		|	|
|	ResourceChange_Refs	|	[[Resource_YieldChange]]	|	✓	|	✓	|		|		|		|	|
|	TerrainChange_Refs	|	[[Terrain_YieldChange]]	|	✓	|	✓	|		|		|		|	|
