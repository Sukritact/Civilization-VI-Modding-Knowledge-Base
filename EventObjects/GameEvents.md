## Static Events
Events can be subscribed by using `GameEvents.SomeEvent.Add(SomeFunction)`.

| Name | Parameters |
|:---- |:--------- |
| [[GameEvents.BuildingConstructed]] | `playerID [number]`<br/>`cityID [number]`<br/>`buildingID [number]`<br/>`plotID [number]`<br/>`bOriginalConstruction [boolean]` |
| [[GameEvents.BuildingPillageStateChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`buildingID [number]`<br/>`bPillageState [boolean]` |
| [[GameEvents.CityBuilt]] | `playerID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[GameEvents.CityConquered]] | `newPlayerID [number]`<br/>`oldPlayerID [number]`<br/>`newCityID [number]`<br/>`iCityX [number]`<br/>`iCityY [number]` |
| [[GameEvents.DiploSurpriseDeclareWar]] | `mainPlayer [number]`<br/>`opponentPlayer [number]` |
| [[GameEvents.EventPopupChoice]] | `playerID [number]`<br/>`tParameters [table]` |
| [[GameEvents.FoundNewWorld]] | `playerID [number]`<br/>`Threshold [number]` |
| [[GameEvents.HasFourCities]] | `playerID [number]`<br/>`Threshold [number]` |
| [[GameEvents.OnCityPopulationChanged]] | `cityOwner [number]`<br/>`cityID [number]`<br/>`ChangeAmount [number]` |
| [[GameEvents.OnCivicCulturevated]] | `iPlayer [number]`<br/>`eCivic [number]` |
| [[GameEvents.OnDistrictConstructed]] | `playerID [number]`<br/>`districtID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[GameEvents.OnFaithEarned]] | `ePlayer [number]`<br/>`iFaithAmount [number]` |
| [[GameEvents.OnGameTurnStarted]] | `playerID [number]` |
| [[GameEvents.OnNewMajorityReligion]] |  |
| [[GameEvents.OnPillage]] | `playerID [number]`<br/>`unitID [number]`<br/>`bImprovement [boolean]`<br/>`buildingType [number]` |
| [[GameEvents.OnPlayerCommandSetObjectState]] | `playerID [number]`<br/>`tParameters [table]` |
| [[GameEvents.OnPlayerGaveInfluenceToken]] | `majorID [number]`<br/>`minorID [number]`<br/>`iAmount [number]` |
| [[GameEvents.OnRandomEventOccurred]] | `iType [number]`<br/>`iSeverity [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`iMitigationLevel [number]` |
| [[GameEvents.OnUnitRetreated]] | `unitOwner [number]`<br/>`unitID [number]` |
| [[GameEvents.PlayerTurnStartComplete]] | `playerID [number]` |
| [[GameEvents.PlayerTurnStarted]] | `playerID [number]` |
| [[GameEvents.PlotOwnershipChanged]] |  |
| [[GameEvents.PlotPropertyChanged]] | `iX [number]`<br/>`iY [number]` |
| [[GameEvents.PolicyChanged]] | `playerID [number]`<br/>`policyID [number]`<br/>`bEnacted [boolean]` |
| [[GameEvents.UnitAddedToMap]] | `playerID [number]`<br/>`unitID [number]` |
