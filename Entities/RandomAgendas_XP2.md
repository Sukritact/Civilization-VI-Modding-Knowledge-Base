---
tags:
- entity
- RandomAgendas_XP2
- XP2
- RandomAgendas
- Random
- Agendas
- XP
- 2
---
# RandomAgendas_XP2
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.RandomAgendas_XP2. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	AgendaType	|	string	|		|		|		|	[[Agenda]].AgendaType	|	✓	|	|
|	AgendaTag	|	string	|		|		|		|	[[AgendaTag]].AgendaTagType	|		|	|
|	RequiresReligion	|	boolean	|		|		|	0	|		|		|	|
|	AgendaReference	|	[[Agenda]]	|		|	✓	|		|		|		|	|
|	RandomAgendaCollection	|	[[RandomAgenda]]	|	✓	|	✓	|		|		|		|	|
