---
tags:
- entity
- TechnologyPrereq
- Technology
- Prereq
---
# TechnologyPrereq
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.TechnologyPrereq. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	Technology	|	string	|		|		|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqTech	|	string	|		|		|		|	[[Technology]].TechnologyType	|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	TechnologyReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
