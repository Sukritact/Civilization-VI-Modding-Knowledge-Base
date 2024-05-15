---
tags:
- entity
- Gossip
---
# Gossip
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Gossip. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	GossipType	|	string	|		|		|		|	[[Type]].Type	|	✓	|	|
|	VisibilityLevel	|	number	|		|		|	0	|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	Message	|	string	|		|		|		|		|		|	|
|	Filter	|	boolean	|		|		|	1	|		|		|	|
|	ErasUntilObsolete	|	number	|		|		|	0	|		|		|	|
|	LevelRequired	|	number	|		|		|	0	|		|		|	|
|	GroupType	|	string	|		|	✓	|		|		|		|	|
