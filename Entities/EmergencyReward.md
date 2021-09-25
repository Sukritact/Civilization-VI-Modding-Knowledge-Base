---
tags:
- entity
- EmergencyReward
- XP2
- XP1
- Emergency
- Reward
---
# EmergencyReward
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.EmergencyReward. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ModifierID	|	string	|		|		|		|	[[Modifier]].ModifierId	|		|	|
|	EmergencyType	|	string	|		|		|		|	[[EmergencyAlliance]].EmergencyType	|		|	|
|	OnSuccess	|	boolean	|		|		|		|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	FirstPlace	|	boolean	|		|		|	0	|		|		|	|
|	TopTier	|	boolean	|		|		|	0	|		|		|	|
|	BottomTier	|	boolean	|		|		|	0	|		|		|	|
