---
tags:
- entity
- AiFavoredItem
- Ai
- Favored
- Item
---
# AiFavoredItem
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.AiFavoredItem. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ListType	|	string	|		|	✓	|		|	[[AiListType]].ListType	|		|	|
|	Item	|	string	|		|		|		|		|		|	|
|	Favored	|	boolean	|		|		|	1	|		|		|	|
|	Value	|	number	|		|		|	0	|		|		|	|
|	StringVal	|	string	|		|	✓	|		|		|		|	|
|	MinDifficulty	|	string	|		|	✓	|		|	[[Difficulty]].DifficultyType	|		|	|
|	MaxDifficulty	|	string	|		|	✓	|		|	[[Difficulty]].DifficultyType	|		|	|
|	TooltipString	|	string	|		|	✓	|		|		|		|	|
|	MaxDifficultyReference	|	[[Difficulty]]	|		|	✓	|		|		|		|	|
|	MinDifficultyReference	|	[[Difficulty]]	|		|	✓	|		|		|		|	|
