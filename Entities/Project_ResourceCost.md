---
tags:
- entity
- Project_ResourceCost
- XP2
- Project
- ResourceCost
- Resource
- Cost
---
# Project_ResourceCost
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Project_ResourceCost. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ProjectType	|	string	|		|		|		|	[[Project]].ProjectType	|		|	|
|	ResourceType	|	string	|		|		|		|	[[Resource]].ResourceType	|		|	|
|	StartProductionCost	|	number	|		|		|		|		|		|	|
|	ProjectReference	|	[[Project]]	|		|	✓	|		|		|		|	|
|	ResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
