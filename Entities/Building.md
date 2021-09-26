---
tags:
- entity
- Building
---
# Building
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Building. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	BuildingType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	Cost	|	number	|		|		|		|		|		|	|
|	MaxPlayerInstances	|	number	|		|		|	-1	|		|		|	|
|	MaxWorldInstances	|	number	|		|		|	-1	|		|		|	|
|	Capital	|	boolean	|		|		|	0	|		|		|	|
|	PrereqDistrict	|	string	|		|	✓	|		|	[[District]].DistrictType	|		|	|
|	AdjacentDistrict	|	string	|		|	✓	|		|	[[District]].DistrictType	|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	RequiresPlacement	|	boolean	|		|		|	0	|		|		|	|
|	RequiresRiver	|	boolean	|		|		|	0	|		|		|	|
|	OuterDefenseHitPoints	|	number	|		|	✓	|		|		|		|	|
|	Housing	|	number	|		|		|	0	|		|		|	|
|	Entertainment	|	number	|		|		|	0	|		|		|	|
|	AdjacentResource	|	string	|		|	✓	|		|	[[Resource]].ResourceType	|		|	|
|	Coast	|	boolean	|		|	✓	|		|		|		|	|
|	EnabledByReligion	|	boolean	|		|		|	0	|		|		|	|
|	AllowsHolyCity	|	boolean	|		|		|	0	|		|		|	|
|	PurchaseYield	|	string	|		|	✓	|		|	[[Yield]].YieldType	|		|	|
|	MustPurchase	|	boolean	|		|		|	0	|		|		|	|
|	Maintenance	|	number	|		|		|	0	|		|		|	|
|	IsWonder	|	boolean	|		|		|	0	|		|		|	|
|	TraitType	|	string	|		|	✓	|		|	[[Trait]].TraitType	|		|	|
|	OuterDefenseStrength	|	number	|		|		|	0	|		|		|	|
|	CitizenSlots	|	number	|		|	✓	|		|		|		|	|
|	MustBeLake	|	boolean	|		|		|	0	|		|		|	|
|	MustNotBeLake	|	boolean	|		|		|	0	|		|		|	|
|	RegionalRange	|	number	|		|		|	0	|		|		|	|
|	AdjacentToMountain	|	boolean	|		|		|	0	|		|		|	|
|	ObsoleteEra	|	string	|		|		|	NO_ERA	|		|		|	|
|	RequiresReligion	|	boolean	|		|		|	0	|		|		|	|
|	GrantFortification	|	number	|		|		|	0	|		|		|	|
|	DefenseModifier	|	number	|		|		|	0	|		|		|	|
|	InternalOnly	|	boolean	|		|		|	0	|		|		|	|
|	RequiresAdjacentRiver	|	boolean	|		|		|	0	|		|		|	|
|	Quote	|	string	|		|	✓	|		|		|		|	|
|	QuoteAudio	|	string	|		|	✓	|		|		|		|	|
|	MustBeAdjacentLand	|	boolean	|		|		|	0	|		|		|	|
|	AdvisorType	|	string	|		|	✓	|		|		|		|	|
|	AdjacentCapital	|	boolean	|		|		|	0	|		|		|	|
|	AdjacentImprovement	|	string	|		|	✓	|		|	[[Improvement]].ImprovementType	|		|	|
|	CityAdjacentTerrain	|	string	|		|	✓	|		|	[[Terrain]].TerrainType	|		|	|
|	UnlocksGovernmentPolicy	|	boolean	|		|	✓	|	0	|		|		|	|
|	GovernmentTierRequirement	|	string	|		|	✓	|		|		|		|	|
|	AdjacentDistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	AdjacentImprovementReference	|	[[Improvement]]	|		|	✓	|		|		|		|	|
|	AdjacentResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
|	CitizenYieldChangesReference	|	[[Building_CitizenYieldChange]]	|	✓	|	✓	|		|		|		|	|
|	CityAdjacentTerrainReference	|	[[Terrain]]	|		|	✓	|		|		|		|	|
|	DependentBuildingCollection	|	[[Building]]	|	✓	|	✓	|		|		|		|	|
|	GreatPersonPointsReference	|	[[Building_GreatPersonPoint]]	|	✓	|	✓	|		|		|		|	|
|	GreatWorkCollection	|	[[Building_GreatWork]]	|	✓	|	✓	|		|		|		|	|
|	MutuallyExclusiveBuildingReference	|	[[MutuallyExclusiveBuilding]]	|	✓	|	✓	|		|		|		|	|
|	PrereqBuildingCollection	|	[[Building]]	|	✓	|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqDistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	PurchaseYieldReference	|	[[Yield]]	|		|	✓	|		|		|		|	|
|	ReplacedByCollection	|	[[BuildingReplace]]	|	✓	|	✓	|		|		|		|	|
|	ReplacesCollection	|	[[BuildingReplace]]	|	✓	|	✓	|		|		|		|	|
|	RequiredFeatures	|	[[Feature]]	|	✓	|	✓	|		|		|		|	|
|	StartingBuildingCollection	|	[[StartingBuilding]]	|	✓	|	✓	|		|		|		|	|
|	TraitReference	|	[[Trait]]	|		|	✓	|		|		|		|	|
|	UnitsPermittedCollection	|	[[Unit]]	|	✓	|	✓	|		|		|		|	|
|	ValidFeatures	|	[[Feature]]	|	✓	|	✓	|		|		|		|	|
|	ValidTerrains	|	[[Terrain]]	|	✓	|	✓	|		|		|		|	|
|	YieldChanges	|	[[Building_YieldChange]]	|	✓	|	✓	|		|		|		|	|
|	YieldDistrictCopyReference	|	[[Building_YieldDistrictCopy]]	|	✓	|	✓	|		|		|		|	|
|	YieldsPerEra	|	[[Building_YieldsPerEra]]	|	✓	|	✓	|		|		|		|	|
