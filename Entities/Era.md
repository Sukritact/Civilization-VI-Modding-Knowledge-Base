---
tags:
- entity
- Era
---
# Era
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Era. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	EraType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	ChronologyIndex	|	number	|		|		|		|		|		|	|
|	WarmongerPoints	|	number	|		|		|	0	|		|		|	|
|	GreatPersonBaseCost	|	number	|		|		|		|		|		|	|
|	EraTechBackgroundTexture	|	string	|		|	✓	|		|		|		|	|
|	EraCivicBackgroundTexture	|	string	|		|	✓	|		|		|		|	|
|	WarmongerLevelDescription	|	string	|		|	✓	|		|		|		|	|
|	EmbarkedUnitStrength	|	number	|		|		|		|		|		|	|
|	EraTechBackgroundTextureOffsetX	|	number	|		|		|	0	|		|		|	|
|	EraCivicBackgroundTextureOffsetX	|	number	|		|		|	0	|		|		|	|
|	TechTreeLayoutMethod	|	number	|		|	✓	|		|		|		|	|
|	BonusMinorStartingUnitCollection	|	[[BonusMinorStartingUnit]]	|	✓	|	✓	|		|		|		|	|
|	CivicCollectionReference	|	[[Civic]]	|	✓	|	✓	|		|		|		|	|
|	MajorStartingUnitCollection	|	[[MajorStartingUnit]]	|	✓	|	✓	|		|		|		|	|
|	StartingBuildingCollection	|	[[StartingBuilding]]	|	✓	|	✓	|		|		|		|	|
|	StartingCivicBoostedCollection	|	[[StartingBoostedCivic]]	|	✓	|	✓	|		|		|		|	|
|	StartingCivicCollection	|	[[StartingCivic]]	|	✓	|	✓	|		|		|		|	|
|	StartingEraCollection	|	[[StartEra]]	|	✓	|	✓	|		|		|		|	|
|	StartingGovernmentCollection	|	[[StartingGovernment]]	|	✓	|	✓	|		|		|		|	|
|	StartingTechnologyBoostedCollection	|	[[StartingBoostedTechnology]]	|	✓	|	✓	|		|		|		|	|
|	TechCollectionReference	|	[[Technology]]	|	✓	|	✓	|		|		|		|	|
