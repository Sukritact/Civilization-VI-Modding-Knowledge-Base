---
tags:
- entity
- ExclusiveAgenda
- Exclusive
- Agenda
---
# ExclusiveAgenda
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.ExclusiveAgenda. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	AgendaOne	|	string	|		|		|		|	[[Agenda]].AgendaType	|		|	|
|	AgendaTwo	|	string	|		|		|		|	[[Agenda]].AgendaType	|		|	|
|	AgendaOneReference	|	[[Agenda]]	|		|	✓	|		|		|		|	|
|	AgendaTwoReference	|	[[Agenda]]	|		|	✓	|		|		|		|	|
