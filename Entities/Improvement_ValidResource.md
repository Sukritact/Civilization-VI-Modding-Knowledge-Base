---
tags:
- entity
- Improvement_ValidResource
- Improvement
- ValidResource
- Valid
- Resource
---
# Improvement_ValidResource
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Improvement_ValidResource. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ImprovementType	|	string	|		|		|		|	[[Improvement]].ImprovementType	|		|	|
|	ResourceType	|	string	|		|		|		|	[[Resource]].ResourceType	|		|	|
|	MustRemoveFeature	|	boolean	|		|		|	1	|		|		|	|
|	ImprovementReference	|	[[Improvement]]	|		|	✓	|		|		|		|	|
|	ResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
