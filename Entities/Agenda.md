---
tags:
- entity
- Agenda
---
# Agenda
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Agenda. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	AgendaType	|	string	|		|		|		|		|	✓	|	|
|	OperationList	|	string	|		|	✓	|		|	[[AiOperationList]].ListType	|		|	|
|	Name	|	string	|		|		|		|		|		|	|
|	Description	|	string	|		|		|		|		|		|	|
|	FirstExclusions	|	[[Agenda]]	|	✓	|	✓	|		|		|		|	|
|	RandomAgendaCollection	|	[[RandomAgenda]]	|	✓	|	✓	|		|		|		|	|
|	SecondExclusions	|	[[Agenda]]	|	✓	|	✓	|		|		|		|	|
|	TraitCollection	|	[[Trait]]	|	✓	|	✓	|		|		|		|	|