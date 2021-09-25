---
tags:
- entity
- UnitAbility
- Unit
- Ability
---
# UnitAbility
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.UnitAbility. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	UnitAbilityType	|	string	|		|		|		|		|		|	|
|	Name	|	[[LocalizedText]]	|		|	✓	|		|		|		|	|
|	Description	|	[[LocalizedText]]	|		|	✓	|		|		|		|	|
|	Inactive	|	boolean	|		|		|	0	|		|		|	|
|	ShowFloatTextWhenEarned	|	boolean	|		|		|	0	|		|		|	|
|	Permanent	|	boolean	|		|		|	1	|		|		|	|
|	UnitAbilityModifierCollection	|	[[UnitAbilityModifier]]	|	✓	|	✓	|		|		|		|	|
