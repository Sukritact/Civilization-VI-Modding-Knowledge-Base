---
tags:
- entity
- AiList
- Ai
- List
---
# AiList
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.AiList. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ListType	|	string	|		|		|		|	[[AiListType]].ListType	|		|	|
|	LeaderType	|	string	|		|	✓	|		|		|		|	|
|	AgendaType	|	string	|		|	✓	|		|		|		|	|
|	System	|	string	|		|		|		|		|		|	|
|	MinDifficulty	|	string	|		|	✓	|		|	[[Difficulty]].DifficultyType	|		|	|
|	MaxDifficulty	|	string	|		|	✓	|		|	[[Difficulty]].DifficultyType	|		|	|
|	MaxDifficultyReference	|	[[Difficulty]]	|		|	✓	|		|		|		|	|
|	MinDifficultyReference	|	[[Difficulty]]	|		|	✓	|		|		|		|	|
