---
tags:
- entity
- GameCapabilityDependency
- Game
- Capability
- Dependency
---
# GameCapabilityDependency
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.GameCapabilityDependency. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	ID	|	number	|		|	✓	|		|		|	✓	|	|
|	GameCapability	|	number	|		|	✓	|		|	[[GameCapability]].GameCapability	|		|	|
|	DependsOnCapability	|	string	|		|	✓	|		|	[[GameCapability]].GameCapability	|		|	|
