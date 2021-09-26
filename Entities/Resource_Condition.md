---
tags:
- entity
- Resource_Condition
- Resource
- Condition
---
# Resource_Condition
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Resource_Condition. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ResourceType	|	string	|		|		|		|	[[Resource]].ResourceType	|	✓	|	|
|	UnlocksFromEffect	|	boolean	|		|		|	0	|		|		|	|
|	ResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
