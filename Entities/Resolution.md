---
tags:
- entity
- Resolution
- XP2
---
# Resolution
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Resolution. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ResolutionType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	TargetKind	|	string	|		|		|		|		|		|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Effect1Description	|	string	|		|	✓	|		|		|		|	|
|	Effect2Description	|	string	|		|	✓	|		|		|		|	|
|	ValidationLua	|	string	|		|	✓	|		|		|		|	|
|	AITargetChooser	|	string	|		|	✓	|		|		|		|	|
|	AILuaTargetChooser	|	string	|		|	✓	|		|		|		|	|
|	InjectionOnly	|	boolean	|		|		|	0	|		|		|	|
|	EarliestEra	|	string	|		|	✓	|		|		|		|	|
|	LatestEra	|	string	|		|	✓	|		|		|		|	|
|	AiChangeCollectionReference	|	[[CongressAiChange]]	|	✓	|	✓	|		|		|		|	|
|	Effects	|	[[ResolutionEffect]]	|	✓	|	✓	|		|		|		|	|
