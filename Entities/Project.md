---
tags:
- entity
- Project
---
# Project
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Project. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ProjectType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	ShortName	|	string	|		|		|		|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	PopupText	|	string	|		|	✓	|		|		|		|	|
|	Cost	|	number	|		|		|		|		|		|	|
|	CostProgressionModel	|	string	|		|		|	NO_PROGRESSION_MODEL	|		|		|	|
|	CostProgressionParam1	|	number	|		|		|	0	|		|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqCivic	|	string	|		|	✓	|		|	[[Civic]].CivicType	|		|	|
|	PrereqDistrict	|	string	|		|	✓	|		|	[[District]].DistrictType	|		|	|
|	RequiredBuilding	|	string	|		|	✓	|		|	[[Building]].BuildingType	|		|	|
|	VisualBuildingType	|	string	|		|	✓	|		|	[[Building]].BuildingType	|		|	|
|	SpaceRace	|	boolean	|		|		|	0	|		|		|	|
|	OuterDefenseRepair	|	boolean	|		|		|	0	|		|		|	|
|	MaxPlayerInstances	|	number	|		|	✓	|		|		|		|	|
|	AmenitiesWhileActive	|	number	|		|	✓	|		|		|		|	|
|	PrereqResource	|	string	|		|	✓	|		|	[[Resource]].ResourceType	|		|	|
|	AdvisorType	|	string	|		|	✓	|		|		|		|	|
|	WMD	|	boolean	|		|		|	0	|		|		|	|
|	UnlocksFromEffect	|	boolean	|		|		|	0	|		|		|	|
|	AntecedantProjectCollectionReference	|	[[ProjectPrereq]]	|	✓	|	✓	|		|		|		|	|
|	GreatPersonPointsReference	|	[[Project_GreatPersonPoint]]	|	✓	|	✓	|		|		|		|	|
|	PrereqCivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	PrereqDistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	PrereqProjectCollectionReference	|	[[ProjectPrereq]]	|	✓	|	✓	|		|		|		|	|
|	PrereqResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	RequiredBuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	VisualBuildingReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	YieldConversionsCollectionReference	|	[[Project_YieldConversion]]	|	✓	|	✓	|		|		|		|	|
