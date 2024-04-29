---
UI: false
arguments:
- MaxInteger [number]
- Reason [string]
invoke: .
memberOf: Game
methodname: GetRandNum
returns:
- RandomInteger [number]
script: true
tags:
- Game/_function
- function/script
---
# Game.GetRandNum
> this function is a member of [[Game]]
> this method can be invoked with `.`
-----
## Usage
| UI  | Script |                  Returns |    Function     | Arguments                                  |
| :-: | :----: | -----------------------: | :-------------: | :----------------------------------------- |
|     |   ✓    | `RandomInteger [number]` | Game.GetRandNum | `MaxInteger [number]`<br>`Reason [string]` |

## Notes
Returns a random integer between 0 and `MaxInteger [number]` - 1 inclusive. So if you feed in 2 as a parameter, it returns either 0 or 1.

If `MaxInteger [number]` is a float, it is rounded down. If it is negative, then it loops around to some unknown positive integer, perhaps 65,535? (max 16 bit digit).