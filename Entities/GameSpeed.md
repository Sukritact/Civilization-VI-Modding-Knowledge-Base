---
tags:
- entity
- GameSpeed
- Game
- Speed
---
# GameSpeed
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.GameSpeed. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	GameSpeedType	|	string	|		|		|		|		|		|	|
|	Name	|	string	|		|	✓	|		|		|		|	|
|	Description	|	string	|		|	✓	|		|		|		|	|
|	CostMultiplier	|	number	|		|		|	100	|		|		|	|
|	CivicUnlockMaxCost	|	number	|		|		|		|		|		|	|
|	CivicUnlockPerTurnDrop	|	number	|		|		|		|		|		|	|
|	CivicUnlockMinCost	|	number	|		|		|		|		|		|	|
|	GameSpeedScalingCollection	|	[[GameSpeed_Scaling]]	|	✓	|	✓	|		|		|		|	|
|	GameSpeedTurnCollection	|	[[GameSpeed_Turn]]	|	✓	|	✓	|		|		|		|	|
