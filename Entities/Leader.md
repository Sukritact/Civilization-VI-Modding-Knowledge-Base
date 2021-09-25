---
tags:
- entity
- Leader
---
# Leader
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Leader. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	LeaderType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	Name	|	string	|		|		|		|		|		|	|
|	OperationList	|	string	|		|	✓	|		|	[[AiOperationList]].ListType	|		|	|
|	IsBarbarianLeader	|	boolean	|		|		|	0	|		|		|	|
|	InheritFrom	|	string	|		|	✓	|		|	[[Leader]].LeaderType	|		|	|
|	SceneLayers	|	number	|		|		|	0	|		|		|	|
|	Sex	|	string	|		|		|	Male	|		|		|	|
|	SameSexPercentage	|	number	|		|		|	0	|		|		|	|
|	CivilizationCollection	|	[[Civilization]]	|	✓	|	✓	|		|		|		|	|
|	InheritLeaderReference	|	[[Leader]]	|		|	✓	|		|		|		|	|
|	PreferredAgendaCollection	|	[[AgendaPreferredLeader]]	|	✓	|	✓	|		|		|		|	|
|	ReligionCollection	|	[[Religion]]	|	✓	|	✓	|		|		|		|	|
|	TraitCollection	|	[[Trait]]	|	✓	|	✓	|		|		|		|	|
