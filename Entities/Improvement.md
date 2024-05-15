---
tags:
- entity
- Improvement
---
# Improvement
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Improvement. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ImprovementType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	BarbarianCamp	|	boolean	|		|		|	0	|		|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	Buildable	|	boolean	|		|		|	0	|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	RemoveOnEntry	|	boolean	|		|		|	0	|		|		|	|
|	DispersalGold	|	number	|		|		|	0	|		|		|	|
|	PlunderType	|	string	|		|		|		|		|		|	|
|	PlunderAmount	|	number	|		|		|	0	|		|		|	|
|	Goody	|	boolean	|		|		|	0	|		|		|	|
|	TilesPerGoody	|	number	|		|	✓	|		|		|		|	|
|	GoodyRange	|	number	|		|	✓	|		|		|		|	|
|	Icon	|	string	|		|		|		|		|		|	|
|	TraitType	|	string	|		|	✓	|		|	[[Trait]].TraitType	|		|	|
|	Housing	|	number	|		|		|	0	|		|		|	|
|	TilesRequired	|	number	|		|		|	1	|		|		|	|
|	SameAdjacentValid	|	boolean	|		|		|	1	|		|		|	|
|	RequiresRiver	|	number	|		|		|	0	|		|		|	|
|	EnforceTerrain	|	boolean	|		|		|	0	|		|		|	|
|	BuildInLine	|	boolean	|		|		|	0	|		|		|	|
|	CanBuildOutsideTerritory	|	boolean	|		|		|	0	|		|		|	|
|	BuildOnFrontier	|	boolean	|		|		|	0	|		|		|	|
|	AirSlots	|	number	|		|		|	0	|		|		|	|
|	DefenseModifier	|	number	|		|		|	0	|		|		|	|
|	GrantFortification	|	number	|		|		|	0	|		|		|	|
|	MinimumAppeal	|	number	|		|	✓	|		|		|		|	|
|	Coast	|	boolean	|		|		|	0	|		|		|	|
|	YieldFromAppeal	|	string	|		|	✓	|		|	[[Yield]].YieldType	|		|	|
|	WeaponSlots	|	number	|		|		|	0	|		|		|	|
|	ReligiousUnitHealRate	|	number	|		|		|	0	|		|		|	|
|	Appeal	|	number	|		|		|	0	|		|		|	|
|	OnePerCity	|	boolean	|		|		|	0	|		|		|	|
|	YieldFromAppealPercent	|	number	|		|		|	100	|		|		|	|
|	ValidAdjacentTerrainAmount	|	number	|		|		|	0	|		|		|	|
|	Domain	|	string	|		|		|	DOMAIN_LAND	|		|		|	|
|	AdjacentSeaResource	|	boolean	|		|		|	0	|		|		|	|
|	RequiresAdjacentBonusOrLuxury	|	boolean	|		|		|	0	|		|		|	|
|	MovementChange	|	number	|		|		|	0	|		|		|	|
|	Workable	|	boolean	|		|		|	1	|		|		|	|
|	ImprovementOnRemove	|	string	|		|	✓	|		|		|		|	|
|	GoodyNotify	|	boolean	|		|		|	1	|		|		|	|
|	NoAdjacentSpecialtyDistrict	|	boolean	|		|		|	0	|		|		|	|
|	RequiresAdjacentLuxury	|	boolean	|		|		|	0	|		|		|	|
|	AdjacentToLand	|	boolean	|		|		|	0	|		|		|	|
|	Removable	|	boolean	|		|		|	1	|		|		|	|
|	OnlyOpenBorders	|	boolean	|		|		|	0	|		|		|	|
|	Capturable	|	boolean	|		|		|	1	|		|		|	|
|	AdjacencyYieldChanges	|	[[Improvement_Adjacency]]	|	✓	|	✓	|		|		|		|	|
|	BonusYieldChanges	|	[[Improvement_BonusYieldChange]]	|	✓	|	✓	|		|		|		|	|
|	InvalidAdjacentFeature	|	[[Improvement_InvalidAdjacentFeature]]	|	✓	|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	TourismCollection	|	[[Improvement_Tourism]]	|	✓	|	✓	|		|		|		|	|
|	TraitReference	|	[[Trait]]	|		|	✓	|		|		|		|	|
|	ValidAdjacentResources	|	[[Improvement_ValidAdjacentResource]]	|	✓	|	✓	|		|		|		|	|
|	ValidAdjacentTerrains	|	[[Improvement_ValidAdjacentTerrain]]	|	✓	|	✓	|		|		|		|	|
|	ValidBuildUnits	|	[[Improvement_ValidBuildUnit]]	|	✓	|	✓	|		|		|		|	|
|	ValidFeatures	|	[[Feature]]	|	✓	|	✓	|		|		|		|	|
|	ValidResources	|	[[Improvement_ValidResource]]	|	✓	|	✓	|		|		|		|	|
|	ValidTerrains	|	[[Terrain]]	|	✓	|	✓	|		|		|		|	|
|	YieldChanges	|	[[Improvement_YieldChange]]	|	✓	|	✓	|		|		|		|	|
|	YieldFromAppealReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
