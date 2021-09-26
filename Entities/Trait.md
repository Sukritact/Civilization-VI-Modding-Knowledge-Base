---
tags:
- entity
- Trait
---
# Trait
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Trait. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	TraitType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	[[LocalizedText]]	|		|	✓	|		|		|		|	|
|	Description	|	[[LocalizedText]]	|		|	✓	|		|		|		|	|
|	InternalOnly	|	boolean	|		|		|	0	|		|		|	|
|	ModifierCollection	|	[[TraitModifier]]	|	✓	|	✓	|		|		|		|	|
