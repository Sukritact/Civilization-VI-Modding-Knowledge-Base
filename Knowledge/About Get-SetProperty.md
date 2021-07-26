# Get/SetProperty

> these methods expect an implicit "self" argument. invoke them with `:`
-----
## Usage
> `Data` Object:GetProperty( `Key [string]` )

> `NULL` Object:SetProperty( `Key [string]`, `Data` )

Get/SetProperty is a useful little method that can be used to store persistent data in [[index#Instances|Instances]] and in the [[Game]] object. Simply provide the key and the data to store with SetProperty, or just the key to retrieve it with GetProperty.

Get/SetProperty always expects an implicit self argument and MUST be called with `:`, even on the Game object.

Properties stored this way are tied to the save file and will persist when the game is closed and the save is reloaded. Properties are accessible by all scripts in all contexts: you can save the data in 

The method can store a large variety of different data types, but notably it can also store Lua tables! So you don't have to store every separate piece of data under a separate key.