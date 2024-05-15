---
tags:
- entity
- GreatPersonIndividual
- Great
- Person
- Individual
---
# GreatPersonIndividual
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.GreatPersonIndividual. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	GreatPersonIndividualType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	GreatPersonClassType	|	string	|		|		|		|	[[GreatPersonClass]].GreatPersonClassType	|		|	|
|	EraType	|	string	|		|		|		|	[[Era]].EraType	|		|	|
|	ActionCharges	|	number	|		|		|		|		|		|	|
|	ActionRequiresOwnedTile	|	boolean	|		|		|	1	|		|		|	|
|	ActionRequiresUnownedTile	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresAdjacentMountain	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresAdjacentOwnedTile	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresAdjacentBarbarianUnit	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresOnOrAdjacentNaturalWonder	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresOnOrAdjacentFeatureType	|	string	|		|	✓	|		|	[[Feature]].FeatureType	|		|	|
|	ActionRequiresIncompleteWonder	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresIncompleteSpaceRaceProject	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresVisibleLuxury	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresNoMilitaryUnit	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresPlayerRelicSlot	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresMilitaryUnitDomain	|	string	|		|	✓	|		|		|		|	|
|	ActionRequiresUnitMilitaryFormation	|	string	|		|	✓	|		|		|		|	|
|	ActionRequiresNearbyUnitWithTagA	|	string	|		|	✓	|		|		|		|	|
|	ActionRequiresNearbyUnitWithTagB	|	string	|		|	✓	|		|		|		|	|
|	ActionRequiresLandMilitaryUnitWithinXTiles	|	number	|		|	✓	|		|		|		|	|
|	ActionRequiresEnemyMilitaryUnitWithinXTiles	|	number	|		|	✓	|		|		|		|	|
|	ActionRequiresCityGreatWorkObjectType	|	string	|		|	✓	|		|	[[GreatWorkObjectType]].GreatWorkObjectType	|		|	|
|	ActionRequiresCompletedDistrictType	|	string	|		|	✓	|		|	[[District]].DistrictType	|		|	|
|	ActionRequiresMissingBuildingType	|	string	|		|	✓	|		|	[[Building]].BuildingType	|		|	|
|	ActionRequiresGoldCost	|	number	|		|	✓	|		|		|		|	|
|	ActionNameTextOverride	|	string	|		|	✓	|		|		|		|	|
|	ActionEffectTextOverride	|	string	|		|	✓	|		|		|		|	|
|	ActionEffectTileHighlighting	|	boolean	|		|		|	1	|		|		|	|
|	BirthNameTextOverride	|	string	|		|	✓	|		|		|		|	|
|	BirthEffectTextOverride	|	string	|		|	✓	|		|		|		|	|
|	AreaHighlightRadius	|	number	|		|	✓	|		|		|		|	|
|	Gender	|	string	|		|		|		|		|		|	|
|	ActionRequiresEnemyTerritory	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresCityStateTerritory	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresNonHostileTerritory	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresSuzerainTerritory	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresUnitCanGainExperience	|	boolean	|		|		|	0	|		|		|	|
|	ActionRequiresCityGreatWorkObjectTypeReference	|	[[GreatWorkObjectType]]	|		|	✓	|		|		|		|	|
|	ActionRequiresCompletedDistrictReference	|	[[District]]	|		|	✓	|		|		|		|	|
|	ActionRequiresMissingBuildingTypeReference	|	[[Building]]	|		|	✓	|		|		|		|	|
|	ActionRequiresOnOrAdjacentFeatureTypeReference	|	[[Feature]]	|		|	✓	|		|		|		|	|
|	EraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	GreatPersonClassReference	|	[[GreatPersonClass]]	|		|	✓	|		|		|		|	|
|	GreatWorkCollection	|	[[GreatWork]]	|	✓	|	✓	|		|		|		|	|
