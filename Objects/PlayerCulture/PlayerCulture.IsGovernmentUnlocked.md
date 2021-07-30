---
UI: true

invoke: ':'
memberOf: Player
methodname: IsGovernmentUnlocked
returns: 
- "IsUnlocked [boolean]"
arguments:
- "GovernmentID [number]"
script: true
tags:
- Player/PlayerCulture/_function
- function/UI
- function/script
---
# PlayerCulture:IsGovernmentUnlocked
> this function is a member of [[PlayerCulture]]
> this method expects an implicit "self" argument. invoke it with `:`
-----
## Usage
|  UI | Script | Returns | Function | Arguments |
|:---:|:------:|-------:|:--------:|:---------|
|✓|✓|`"IsUnlocked [boolean]"`|PlayerCulture:IsGovernmentUnlocked|`"GovernmentID [number]"`|

## Notes
`GovernmentID [number]` is a row identifier for the `Governments` table.

 `GovernmentID` can be either the row  `Index` or the row `Hash` in UI scripts.
 
 `GovernmentID` MUST be the row `Index` in gameplay scripts: using the `Hash` will cause the game to crash.
