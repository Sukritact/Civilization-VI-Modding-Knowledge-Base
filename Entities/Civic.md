---
tags:
- entity
- Civic
---
# Civic
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Civic. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	CivicType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Cost	|	number	|		|		|		|		|		|	|
|	Repeatable	|	boolean	|		|		|	0	|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	EraType	|	string	|		|		|		|	[[Era]].EraType	|		|	|
|	BarbarianFree	|	boolean	|		|		|	0	|		|		|	|
|	UITreeRow	|	number	|		|	✓	|	0	|		|		|	|
|	AdvisorType	|	string	|		|	✓	|		|		|		|	|
|	EmbarkAll	|	boolean	|		|		|	0	|		|		|	|
|	EmbarkUnitType	|	string	|		|	✓	|		|		|		|	|
|	BoostCollectionRef	|	[[Boost]]	|	✓	|	✓	|		|		|		|	|
|	BuildingCollectionReference	|	[[Building]]	|	✓	|	✓	|		|		|		|	|
|	DistrictCollectionReference	|	[[District]]	|	✓	|	✓	|		|		|		|	|
|	EraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	GovernmentCollection	|	[[Government]]	|	✓	|	✓	|		|		|		|	|
|	ImprovementTourismCollection	|	[[Improvement_Tourism]]	|	✓	|	✓	|		|		|		|	|
|	MandatoryObsoleteCivicCollection	|	[[Unit]]	|	✓	|	✓	|		|		|		|	|
|	ObsoleteCivicCollection	|	[[Unit]]	|	✓	|	✓	|		|		|		|	|
|	PolicyCollection	|	[[Policy]]	|	✓	|	✓	|		|		|		|	|
|	PrereqCivicCollection	|	[[CivicPrereq]]	|	✓	|	✓	|		|		|		|	|
|	StartingCivicCollection	|	[[StartingCivic]]	|	✓	|	✓	|		|		|		|	|
|	UnitCollection	|	[[Unit]]	|	✓	|	✓	|		|		|		|	|
