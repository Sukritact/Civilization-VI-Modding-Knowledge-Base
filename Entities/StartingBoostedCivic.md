---
tags:
- entity
- StartingBoostedCivic
- Starting
- Boosted
- Civic
---
# StartingBoostedCivic
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.StartingBoostedCivic. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Civic	|	string	|		|		|	NO_CIVIC	|	[[Civic]].CivicType	|		|	|
|	Era	|	string	|		|		|		|	[[Era]].EraType	|		|	|
|	CivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	EraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
