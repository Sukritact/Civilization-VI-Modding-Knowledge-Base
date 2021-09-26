---
tags:
- entity
- DiplomaticVisibilitySource
- Diplomatic
- Visibility
- Source
---
# DiplomaticVisibilitySource
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.DiplomaticVisibilitySource. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	VisibilitySourceType	|	string	|		|		|		|		|	✓	|	|
|	Description	|	string	|		|		|		|		|		|	|
|	ActionDescription	|	string	|		|		|		|		|		|	|
|	GossipString	|	string	|		|		|		|		|		|	|
|	Trader	|	boolean	|		|		|	0	|		|		|	|
|	Delegate	|	boolean	|		|		|	0	|		|		|	|
|	Ally	|	boolean	|		|		|	0	|		|		|	|
|	Spy	|	boolean	|		|		|	0	|		|		|	|
|	PrereqTech	|	string	|		|	✓	|		|	[[Technology]].TechnologyType	|		|	|
|	TraitType	|	string	|		|	✓	|		|	[[Trait]].TraitType	|		|	|
|	GreatPersonIndividualType	|	string	|		|	✓	|		|	[[GreatPersonIndividual]].GreatPersonIndividualType	|		|	|
|	FromCitizen	|	boolean	|		|		|	0	|		|		|	|
|	LevelRequired	|	number	|		|		|	0	|		|		|	|
|	GreatPersonIndividualReference	|	[[GreatPersonIndividual]]	|		|	✓	|		|		|		|	|
|	PrereqTechReference	|	[[Technology]]	|		|	✓	|		|		|		|	|
|	TraitReference	|	[[Trait]]	|		|	✓	|		|		|		|	|
