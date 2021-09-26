---
tags:
- entity
- District
---
# District
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.District. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	DistrictType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	Coast	|	boolean	|		|		|	0	|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	Cost	|	number	|		|		|	0	|		|		|	|
|	RequiresPlacement	|	boolean	|		|		|		|		|		|	|
|	RequiresPopulation	|	boolean	|		|		|	1	|		|		|	|
|	NoAdjacentCity	|	boolean	|		|		|		|		|		|	|
|	CityCenter	|	boolean	|		|		|	0	|		|		|	|
|	Aqueduct	|	boolean	|		|		|		|		|		|	|
|	InternalOnly	|	boolean	|		|		|		|		|		|	|
|	ZOC	|	boolean	|		|	✓	|	0	|		|		|	|
|	FreeEmbark	|	boolean	|		|		|	0	|		|		|	|
|	HitPoints	|	number	|		|	✓	|	0	|		|		|	|
|	CaptureRemovesBuildings	|	boolean	|		|		|		|		|		|	|
|	CaptureRemovesCityDefenses	|	boolean	|		|		|		|		|		|	|
|	PlunderType	|	string	|		|		|		|		|		|	|
|	PlunderAmount	|	number	|		|		|	0	|		|		|	|
|	TradeEmbark	|	boolean	|		|		|	0	|		|		|	|
|	MilitaryDomain	|	string	|		|		|		|		|		|	|
|	CostProgressionModel	|	string	|		|		|	NO_COST_PROGRESSION	|		|		|	|
|	CostProgressionParam1	|	number	|		|		|	0	|		|		|	|
|	TraitType	|	string	|		|	✓	|		|	[[Trait]].TraitType	|		|	|
|	Appeal	|	number	|		|		|	0	|		|		|	|
|	Housing	|	number	|		|		|	0	|		|		|	|
|	Entertainment	|	number	|		|		|	0	|		|		|	|
|	OnePerCity	|	boolean	|		|		|	1	|		|		|	|
|	AllowsHolyCity	|	boolean	|		|		|	0	|		|		|	|
|	Maintenance	|	number	|		|		|	0	|		|		|	|
|	AirSlots	|	number	|		|		|	0	|		|		|	|
|	CitizenSlots	|	number	|		|	✓	|		|		|		|	|
|	TravelTime	|	number	|		|		|	-1	|		|		|	|
|	CityStrengthModifier	|	number	|		|		|	0	|		|		|	|
|	AdjacentToLand	|	boolean	|		|		|	0	|		|		|	|
|	CanAttack	|	boolean	|		|		|	0	|		|		|	|
|	AdvisorType	|	string	|		|	✓	|		|		|		|	|
|	CaptureRemovesDistrict	|	boolean	|		|		|	0	|		|		|	|
|	MaxPerPlayer	|	number	|		|		|	-1	|		|		|	|
|	AdjacencyAppealYieldChanges	|	[[Adjacent_AppealYieldChange]]	|	✓	|	✓	|		|		|		|	|
|	AdjacencyYieldChanges	|	[[District_Adjacency]]	|	✓	|	✓	|		|		|		|	|
|	AppealHousingChangeReference	|	[[AppealHousingChange]]	|	✓	|	✓	|		|		|		|	|
|	BuildingCollectionReference	|	[[Building]]	|	✓	|	✓	|		|		|		|	|
|	CitizenGreatPersonPointsReference	|	[[District_CitizenGreatPersonPoint]]	|	✓	|	✓	|		|		|		|	|
|	CitizenYieldChangesReference	|	[[District_CitizenYieldChange]]	|	✓	|	✓	|		|		|		|	|
|	ExclusionReference	|	[[ExcludedDistrict]]	|	✓	|	✓	|		|		|		|	|
|	GreatPersonPointsReference	|	[[District_GreatPersonPoint]]	|	✓	|	✓	|		|		|		|	|
|	MutuallyExclusiveDistrictReference	|	[[MutuallyExclusiveDistrict]]	|	✓	|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	ProjectCollection	|	[[Project]]	|	✓	|	✓	|		|		|		|	|
|	ReplacedByCollection	|	[[DistrictReplace]]	|	✓	|	✓	|		|		|		|	|
|	ReplacesCollection	|	[[DistrictReplace]]	|	✓	|	✓	|		|		|		|	|
|	RequiredFeatures	|	[[Feature]]	|	✓	|	✓	|		|		|		|	|
|	StartingBuildingCollection	|	[[StartingBuilding]]	|	✓	|	✓	|		|		|		|	|
|	TradeRouteYieldChanges	|	[[District_TradeRouteYield]]	|	✓	|	✓	|		|		|		|	|
|	TraitReference	|	[[Trait]]	|		|	✓	|		|		|		|	|
|	ValidTerrains	|	[[Terrain]]	|	✓	|	✓	|		|		|		|	|
