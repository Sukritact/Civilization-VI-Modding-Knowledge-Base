---
tags:
- entity
- StartingBoostedTechnology
- Starting
- Boosted
- Technology
---
# StartingBoostedTechnology
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.StartingBoostedTechnology. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Technology	|	string	|		|		|	NO_TECHNOLOGY	|	[[Technology]].TechnologyType	|		|	|
|	Era	|	string	|		|		|		|	[[Era]].EraType	|		|	|
|	EraReference	|	[[Era]]	|		|	✓	|		|		|		|	|
|	TechnologyReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
