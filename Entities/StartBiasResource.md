---
tags:
- entity
- StartBiasResource
- Start
- Bias
- Resource
---
# StartBiasResource
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.StartBiasResource. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	CivilizationType	|	string	|		|		|		|	[[Civilization]].CivilizationType	|		|	|
|	ResourceType	|	string	|		|		|		|	[[Resource]].ResourceType	|		|	|
|	Tier	|	number	|		|		|	-1	|		|		|	|
|	CivilizationReference	|	[[Civilization]]	|		|	✓	|		|		|		|	|
|	ResourceReference	|	[[Resource]]	|		|	✓	|		|		|		|	|
