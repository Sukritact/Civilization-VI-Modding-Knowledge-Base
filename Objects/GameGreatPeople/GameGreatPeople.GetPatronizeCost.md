---
UI: true
arguments:
- PlayerID [number]
- IndividualID [number]
- YieldType [number]
invoke: ':'
memberOf: Game/GameGreatPeople
methodname: GetPatronizeCost
returns: []
script: true
tags:
- Game/GameGreatPeople/_function
- function/UI
- function/script
---
# GameGreatPeople:GetPatronizeCost
> this function is a member of [[GameGreatPeople]]
> this method expects an implicit "self" argument. invoke it with `:`
-----
## Usage
|  UI | Script | Returns | Function | Arguments |
|:---:|:------:|-------:|:--------:|:---------|
|✓|✓||GameGreatPeople:GetPatronizeCost|`PlayerID [number]`<br>`IndividualID [number]`<br>`YieldType [number]`|

## Notes
  
`YieldType [number]` corresponds to an entry in the `YieldTypes` global table, NOT the Index of the yield in the game database.

For instance, see this code sample:

> `pGreatPeople:GetPatronizeCost(displayPlayerID, entry.Individual, YieldTypes.GOLD)`

