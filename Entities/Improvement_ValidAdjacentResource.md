---
tags:
- entity
- Improvement_ValidAdjacentResource
- Improvement
- ValidAdjacentResource
- Valid
- Adjacent
- Resource
---
# Improvement_ValidAdjacentResource
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Improvement_ValidAdjacentResource. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ImprovementType	|	string	|		|		|		|	[[Improvement]].ImprovementType	|		|	|
|	ResourceType	|	string	|		|		|		|	[[Resource]].ResourceType	|		|	|
|	ImprovementReference	|	[[Improvement]]	|		|	✓	|		|		|		|	|
|	ResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
