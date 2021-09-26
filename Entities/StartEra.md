---
tags:
- entity
- StartEra
- Start
- Era
---
# StartEra
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.StartEra. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	EraType	|	string	|		|		|		|	[[Era]].EraType	|	✓	|	|
|	Gold	|	number	|		|		|	0	|		|		|	|
|	Faith	|	number	|		|		|	0	|		|		|	|
|	FirstTurnCivicChange	|	boolean	|		|		|	0	|		|		|	|
|	StartingPopulationCapital	|	number	|		|		|	1	|		|		|	|
|	StartingPopulationOtherCities	|	number	|		|		|	1	|		|		|	|
|	GrowthRate	|	number	|		|		|	0	|		|		|	|
|	ProductionRate	|	number	|		|		|	0	|		|		|	|
|	DistrictProductionRate	|	number	|		|		|	0	|		|		|	|
|	StartingMeleeStrengthMajor	|	number	|		|		|	0	|		|		|	|
|	StartingMeleeStrengthMinor	|	number	|		|		|	0	|		|		|	|
|	ObsoleteReligion	|	boolean	|		|		|	0	|		|		|	|
|	Tiles	|	number	|		|		|	0	|		|		|	|
|	Year	|	number	|		|		|		|		|		|	|
|	IgnoreGoodyHutTurn	|	boolean	|		|		|	0	|		|		|	|
|	StartingRangedStrengthMajor	|	number	|		|		|	0	|		|		|	|
|	StartingRangedStrengthMinor	|	number	|		|		|	0	|		|		|	|
|	StartingAmenitiesCapital	|	number	|		|		|	0	|		|		|	|
|	StartingHousingCapital	|	number	|		|		|	0	|		|		|	|
|	StartingAmenitiesOtherCities	|	number	|		|		|	0	|		|		|	|
|	StartingHousingOtherCities	|	number	|		|		|	0	|		|		|	|
|	EraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
