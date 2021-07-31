---
UI: true
arguments:
- GovernmentID [number]
invoke: ':'
memberOf: Player/PlayerCulture
methodname: IsGovernmentUnlocked
returns:
- IsUnlocked [boolean]
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
|✓|✓|`IsUnlocked [boolean]`|PlayerCulture:IsGovernmentUnlocked|`GovernmentID [number]`|
