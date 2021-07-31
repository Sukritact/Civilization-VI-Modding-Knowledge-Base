---
UI: false
arguments:
- MaxInteger [number]
- Reason [string]
invoke: .
memberOf: TerrainBuilder
methodname: GetRandomNumber
returns:
- RandomInteger [number]
script: true
tags:
- TerrainBuilder/_function
- function/script
---
# TerrainBuilder.GetRandomNumber
> this function is a member of [[TerrainBuilder]]
> this method can be invoked with `.`
-----
## Usage
|  UI | Script | Returns | Function | Arguments |
|:---:|:------:|-------:|:--------:|:---------|
| |✓|`RandomInteger [number]`|TerrainBuilder.GetRandomNumber|`MaxInteger [number]`<br>`Reason [string]`|

## Notes
Returns a random integer between 0 and `MaxInteger [number]` - 1 inclusive. So if you feed in 2 as a parameter, it returns either 0 or 1.