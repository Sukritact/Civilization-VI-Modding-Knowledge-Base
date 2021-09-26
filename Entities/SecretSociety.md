---
tags:
- entity
- SecretSociety
- XP2
- XP1
- Secret
- Society
---
# SecretSociety
## Entity
This file is a description of an Entity's properties. There is no accessible variable of this name, rather, these entities must be retrieved from GameData.SecretSociety. Accessing a property should be invoked with a `.`.
## Properties
|	Property	|	Type	|	Collection Of Type?	|	May Be Nil?	|	Default	|	References	|	Key	|	Notes	|
|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	:-:	|	-:	|
|	SecretSocietyType	|	string	|		|		|		|		|	✓	|	|
|	Name	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	Description	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	DiscoveryText	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	MembershipText	|	[[LocalizedText]]	|		|		|		|		|		|	|
|	GovernorType	|	string	|		|	✓	|		|	[[Governor]].GovernorType	|		|	|
|	DiscoverAtBarbarianCampBaseChance	|	number	|		|		|	0	|		|		|	|
|	DiscoverAtCityStateBaseChance	|	number	|		|		|	0	|		|		|	|
|	DiscoverAtGoodyHutBaseChance	|	number	|		|		|	0	|		|		|	|
|	DiscoverAtNaturalWonderBaseChance	|	number	|		|		|	0	|		|		|	|
|	SmallIcon	|	string	|		|		|		|		|		|	|
|	IconString	|	string	|		|		|		|		|		|	|
|	GovernorReference	|	[[Governor]]	|		|	✓	|		|		|		|	|
