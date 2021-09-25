---
tags:
- entity
- UnitAiInfo
- Unit
- Ai
- Info
---
# UnitAiInfo
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.UnitAiInfo. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	UnitType	|	string	|		|		|		|	[[Unit]].UnitType	|		|	|
|	AiType	|	string	|		|		|		|	[[UnitAiType]].AiType	|		|	|
|	UnitAiTypeReference	|	[[UnitAiType]]	|		|	✓	|		|		|		|	|
