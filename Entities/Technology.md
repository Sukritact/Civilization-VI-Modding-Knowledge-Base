---
tags:
- entity
- Technology
---
# Technology
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Technology. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TechnologyType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Cost	|	number	|		|		|		|		|		|	|
|	Repeatable	|	boolean	|		|		|	0	|		|		|	|
|	EmbarkUnitType	|	string	|		|	✓	|		|	[[Unit]].UnitType	|		|	|
|	EmbarkAll	|	boolean	|		|		|	0	|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	EraType	|	string	|		|		|		|	[[Era]].EraType	|		|	|
|	Critical	|	boolean	|		|		|	0	|		|		|	|
|	BarbarianFree	|	boolean	|		|		|	0	|		|		|	|
|	UITreeRow	|	number	|		|	✓	|	0	|		|		|	|
|	AdvisorType	|	string	|		|	✓	|		|		|		|	|
|	BoostCollectionReference	|	[[Boost]]	|	✓	|	✓	|		|		|		|	|
|	BuildingCollectionReference	|	[[Building]]	|	✓	|	✓	|		|		|		|	|
|	DistrictCollectionReference	|	[[District]]	|	✓	|	✓	|		|		|		|	|
|	EmbarkUnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
|	EraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	ImprovementCollection	|	[[Improvement]]	|	✓	|	✓	|		|		|		|	|
|	ImprovementTourismCollection	|	[[Improvement_Tourism]]	|	✓	|	✓	|		|		|		|	|
|	MandatoryObsoleteTechCollection	|	[[Unit]]	|	✓	|	✓	|		|		|		|	|
|	ObsoleteTechCollection	|	[[Unit]]	|	✓	|	✓	|		|		|		|	|
|	PolicyCollection	|	[[Policy]]	|	✓	|	✓	|		|		|		|	|
|	PrereqTechCollection	|	[[TechnologyPrereq]]	|	✓	|	✓	|		|		|		|	|
|	ProjectCollection	|	[[Project]]	|	✓	|	✓	|		|		|		|	|
|	UnitCollection	|	[[Unit]]	|	✓	|	✓	|		|		|		|	|
