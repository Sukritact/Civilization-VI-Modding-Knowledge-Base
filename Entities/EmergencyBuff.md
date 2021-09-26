---
tags:
- entity
- EmergencyBuff
- XP2
- XP1
- Emergency
- Buff
---
# EmergencyBuff
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.EmergencyBuff. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ModifierID	|	string	|		|		|		|	[[Modifier]].ModifierId	|		|	|
|	EmergencyType	|	string	|		|		|		|	[[EmergencyAlliance]].EmergencyType	|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	EmergencyRef	|	[[EmergencyAlliance]]	|		|	✓	|		|		|		|	|
