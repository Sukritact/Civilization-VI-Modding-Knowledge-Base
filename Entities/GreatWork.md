---
tags:
- entity
- GreatWork
- Great
- Work
---
# GreatWork
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.GreatWork. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	GreatWorkType	|	string	|		|		|		|		|	✓	|	|
|	GreatWorkObjectType	|	string	|		|		|		|	[[GreatWorkObjectType]].GreatWorkObjectType	|		|	|
|	GreatPersonIndividualType	|	string	|		|	✓	|		|	[[GreatPersonIndividual]].GreatPersonIndividualType	|		|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Audio	|	string	|		|	✓	|		|		|		|	|
|	Image	|	string	|		|	✓	|		|		|		|	|
|	Quote	|	string	|		|	✓	|		|		|		|	|
|	Tourism	|	number	|		|		|	1	|		|		|	|
|	EraType	|	string	|		|	✓	|		|	[[Era]].EraType	|		|	|
|	BuildingCollection	|	[[Building]]	|	✓	|	✓	|		|		|		|	|
|	EraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	GreatPersonReference	|	[[GreatPersonIndividual]]	|		|	✓	|		|		|		|	|
|	GreatWorkObjectReference	|	[[GreatWorkObjectType]]	|		|	✓	|		|		|		|	|
|	YieldChanges	|	[[GreatWork_YieldChange]]	|	✓	|	✓	|		|		|		|	|
