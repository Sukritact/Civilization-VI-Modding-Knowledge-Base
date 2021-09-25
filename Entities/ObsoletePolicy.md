---
tags:
- entity
- ObsoletePolicy
- Obsolete
- Policy
---
# ObsoletePolicy
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.ObsoletePolicy. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	PolicyType	|	string	|		|		|		|	[[Policy]].PolicyType	|		|	|
|	ObsoletePolicy	|	string	|		|	✓	|		|	[[Policy]].PolicyType	|		|	|
|	RequiresAvailableGreatPersonClass	|	string	|		|	✓	|		|	[[GreatPersonClass]].GreatPersonClassType	|		|	|
|	ObsoletePolicyReference	|	[[Policy]]	|		|	✓	|		|		|		|	|
|	PolicyReference	|	[[Policy]]	|		|	✓	|		|		|		|	|
|	RequiresAvailableGreatPersonClassReference	|	[[GreatPersonClass]]	|		|	✓	|		|		|		|	|
