---
tags:
- entity
- RandomAgendasForCivic
- XP2
- Random
- Agendas
- for
- Civic
---
# RandomAgendasForCivic
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.RandomAgendasForCivic. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	CivicType	|	string	|		|		|		|	[[Civic]].CivicType	|	✓	|	|
|	NumAgendas	|	number	|		|		|	1	|		|		|	|
|	VisibilityType	|	string	|		|		|		|	[[Visibility]].VisibilityType	|		|	|
|	AgendaTagCollection	|	[[AgendaTag]]	|	✓	|	✓	|		|		|		|	|
|	CivicReference	|	[[Civic]]	|		|	✓	|		|		|		|	|
|	VisibilityReference	|	[[Visibility]]	|		|	✓	|		|		|		|	|
