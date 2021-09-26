---
tags:
- entity
- Belief
---
# Belief
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Belief. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	BeliefType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Description	|	string	|		|		|		|		|		|	|
|	BeliefClassType	|	string	|		|		|		|	[[BeliefClass]].BeliefClassType	|		|	|
|	BeliefClassTypeReference	|	[[BeliefClass]]	|		|	✓	|		|		|		|	|
