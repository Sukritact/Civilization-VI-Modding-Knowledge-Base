---
tags:
- entity
- Route_ValidBuildUnit
- Route
- ValidBuildUnit
- Valid
- Build
- Unit
---
# Route_ValidBuildUnit
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.Route_ValidBuildUnit. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	RouteType	|	string	|		|		|		|	[[Route]].RouteType	|		|	|
|	UnitType	|	string	|		|		|		|	[[Unit]].UnitType	|		|	|
|	RouteReference	|	[[Route]]	|		|	✓	|		|		|		|	|
|	UnitReference	|	[[Unit]]	|		|	✓	|		|		|		|	|
