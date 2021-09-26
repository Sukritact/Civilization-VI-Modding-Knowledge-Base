---
tags:
- entity
- Resource
---
# Resource
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Resource. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ResourceType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	ResourceClassType	|	string	|		|		|		|		|		|	|
|	Happiness	|	number	|		|		|	0	|		|		|	|
|	NoRiver	|	boolean	|		|		|	0	|		|		|	|
|	RequiresRiver	|	boolean	|		|		|	0	|		|		|	|
|	Frequency	|	number	|		|		|	0	|		|		|	|
|	Clumped	|	boolean	|		|		|	0	|		|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	PeakEra	|	string	|		|		|	NO_ERA	|		|		|	|
|	RevealedEra	|	number	|		|		|	1	|		|		|	|
|	LakeEligible	|	boolean	|		|		|	1	|		|		|	|
|	AdjacentToLand	|	boolean	|		|		|	0	|		|		|	|
|	SeaFrequency	|	number	|		|		|	0	|		|		|	|
|	Harvests	|	[[Resource_Harvest]]	|	✓	|	✓	|		|		|		|	|
|	ImprovementAdjacentResourceCollection	|	[[Improvement_ValidAdjacentResource]]	|	✓	|	✓	|		|		|		|	|
|	ImprovementCollection	|	[[Improvement_ValidResource]]	|	✓	|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	ResourceProjectCollection	|	[[Project]]	|	✓	|	✓	|		|		|		|	|
|	StartBiasResourceCollection	|	[[StartBiasResource]]	|	✓	|	✓	|		|		|		|	|
|	StrategicUnitCollection	|	[[Unit]]	|	✓	|	✓	|		|		|		|	|
|	TradeRouteYieldChanges	|	[[Resource_TradeRouteYield]]	|	✓	|	✓	|		|		|		|	|
|	ValidTerrains	|	[[Terrain]]	|	✓	|	✓	|		|		|		|	|
|	YieldChangeCollection	|	[[Resource_YieldChange]]	|	✓	|	✓	|		|		|		|	|
