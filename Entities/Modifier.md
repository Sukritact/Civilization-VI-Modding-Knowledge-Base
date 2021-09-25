---
tags:
- entity
- Modifier
---
# Modifier
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Modifier. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ModifierId	|	string	|		|		|		|		|	✓	|	|
|	ModifierType	|	string	|		|		|		|		|		|	|
|	RunOnce	|	boolean	|		|		|	0	|		|		|	|
|	NewOnly	|	boolean	|		|		|	0	|		|		|	|
|	Permanent	|	boolean	|		|		|	0	|		|		|	|
|	Repeatable	|	boolean	|		|	✓	|	0	|		|		|	|
|	OwnerRequirementSetId	|	string	|		|	✓	|		|	[[RequirementSet]].RequirementSetId	|		|	|
|	SubjectRequirementSetId	|	string	|		|	✓	|		|	[[RequirementSet]].RequirementSetId	|		|	|
|	OwnerStackLimit	|	number	|		|	✓	|		|		|		|	|
|	SubjectStackLimit	|	number	|		|	✓	|		|		|		|	|
