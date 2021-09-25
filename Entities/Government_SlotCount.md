---
tags:
- entity
- Government_SlotCount
- Government
- SlotCount
- Slot
- Count
---
# Government_SlotCount
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Government_SlotCount. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	GovernmentType	|	string	|		|		|		|	[[Government]].GovernmentType	|		|	|
|	GovernmentSlotType	|	string	|		|		|		|	[[GovernmentSlot]].GovernmentSlotType	|		|	|
|	NumSlots	|	number	|		|		|		|		|		|	|
|	GovernmentReference	|	[[Government]]	|		|	✓	|		|		|		|	|
|	SlotReference	|	[[GovernmentSlot]]	|		|	✓	|		|		|		|	|
