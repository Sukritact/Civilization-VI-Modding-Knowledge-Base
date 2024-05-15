---
tags:
- entity
- Notification
---
# Notification
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Notification. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	NotificationType	|	string	|		|		|		|		|		|	|
|	Message	|	string	|		|	✓	|		|		|		|	|
|	Summary	|	string	|		|	✓	|		|		|		|	|
|	SeverityType	|	string	|		|	✓	|		|		|		|	|
|	ExpiresEndOfTurn	|	boolean	|		|		|	1	|		|		|	|
|	ExpiresEndOfNextTurn	|	boolean	|		|		|	0	|		|		|	|
|	SubType	|	string	|		|	✓	|		|		|		|	|
|	AutoNotify	|	boolean	|		|		|	0	|		|		|	|
|	GroupType	|	string	|		|	✓	|		|		|		|	|
|	Icon	|	string	|		|	✓	|		|		|		|	|
|	AutoActivate	|	boolean	|		|		|	0	|		|		|	|
|	VisibleInUI	|	boolean	|		|		|	1	|		|		|	|
|	ShowIconSinglePlayer	|	boolean	|		|		|	1	|		|		|	|
