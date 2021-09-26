---
tags:
- entity
- StartingGovernment
- Starting
- Government
---
# StartingGovernment
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.StartingGovernment. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Government	|	string	|		|		|	NO_GOVERNMENT	|	[[Government]].GovernmentType	|		|	|
|	Era	|	string	|		|		|		|	[[Era]].EraType	|		|	|
|	Change	|	boolean	|		|		|	0	|		|		|	|
|	EraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	GovernmentReference	|	[[Government]]	|		|	✓	|		|		|		|	|
