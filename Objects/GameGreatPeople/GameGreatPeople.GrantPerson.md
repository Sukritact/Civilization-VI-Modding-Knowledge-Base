---
UI: false
arguments:
- IndividualID [number]
- GreatPersonClassID [number]
- EraID [number]
- Cost [number]
- PlayerID [number]
- Unknown [boolean]
invoke: ':'
memberOf: Game
methodname: GrantPerson
returns: []
script: true
tags:
- Game/GameGreatPeople/_function
- function/script
---
# GameGreatPeople:GrantPerson
> this function is a member of [[GameGreatPeople]]
> this method expects an implicit "self" argument. invoke it with `:`
-----
## Usage
|  UI | Script | Returns | Function | Arguments |
|:---:|:------:|-------:|:--------:|:---------|
|✓| ||GameGreatPeople:GrantPerson|`IndividualID [number]`<br>`GreatPersonClassID [number]`<br>`EraID [number]`<br>`Cost [number]`<br>`PlayerID [number]`<br>`Unknown [boolean]`|

## Notes
Grants the specified Great Person Individual. The Great Person seems to be placed in the most appropriate location as it would be were the Great Person earned via normal gameplay.

Great Person Recruitment history is updated, and it prevents the same Great Person Individual from being earned normally through gameplay. This contrasts with [[GameGreatPeople.CreatePerson]] which doesn't. However, it is possible to create multiple of the same Great Person this way.

### Parameters
- `IndividualID [number]`
	- Corresponds to a an `Index` or `Hash` column in the `GreatPersonIndividuals` table
- `GreatPersonClassID [number]`
	- Corresponds to a an `Index` or `Hash` column in the `GreatPersonClasses` table
- `EraID [number]`
	- Corresponds to a an `Index` or `Hash` column in the `Eras` table
- `Cost [number]`
	- Cost to recruit the Great Person (?)
- `PlayerID [number]`
- `Unknown [boolean]`

`GreatPersonClassID`, `EraID`, and `Cost` seem to only be for Recruitment History purposes. A mismatch bewteen the `IndividualID` and the `GreatPersonClassID` will still spawn the Great Person correctly for instance, but the Recruitment History will show the incorrect Great Person Class.