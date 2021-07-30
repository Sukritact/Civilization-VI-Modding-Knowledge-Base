# Events
## Usage
This object exposes events designed to make the UI react to data changes. You may try to use them to implement gameplay changes.

## Static Events
Events can be subscribed by using `Events.SomeEvent.Add(SomeFunction)`.

| Name | Parameters |
|:---- |:--------- |
| [[Events.AllianceAvailable]] | `playerID [number]`<br/>`otherplayerID [number]`<br/>`AllianceType [number]` |
| [[Events.AllianceEnded]] | `playerID [number]`<br/>`otherplayerID [number]`<br/>`AllianceType [number]` |
| [[Events.AnarchyBegins]] |  |
| [[Events.AnarchyEnds]] |  |
| [[Events.BarbarianRaidStarted]] |  |
| [[Events.BarbarianSpottedCity]] | `playerID [number]`<br/>`unitID [number]`<br/>`cityOwner [number]`<br/>`cityID [number]` |
| [[Events.BeginWonderReveal]] |  |
| [[Events.BeliefAdded]] | `playerID [number]`<br/>`beliefID [number]` |
| [[Events.BuildingAddedToMap]] | `iX [number]`<br/>`iY [number]`<br/>`buildingID [number]`<br/>`playerID [number]`<br/>`misc2`<br/>`misc3` |
| [[Events.BuildingBuildProgressChanged]] |  |
| [[Events.BuildingChanged]] | `iX [number]`<br/>`iY [number]`<br/>`buildingID [number]`<br/>`playerID [number]`<br/>`iPercentComplete [number]`<br/>`iUnknown` |
| [[Events.BuildingPillaged]] |  |
| [[Events.BuildingRemovedFromMap]] | `iX [number]`<br/>`iY [number]` |
| [[Events.BuildingVisibilityChanged]] |  |
| [[Events.CacheUpdate]] |  |
| [[Events.CameraUpdated]] | `vFocusX [number]`<br/>`vFocusY [number]`<br/>`fZoomLevel [number]` |
| [[Events.CapitalCityChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[Events.CityAddedToMap]] | `playerID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[Events.CityChanged]] |  |
| [[Events.CityCommandStarted]] | `cityOwnerID [number]`<br/>`cityID [number]`<br/>`districtOwnerID [number]`<br/>`commandType [number]`<br/>`iData1 [number]` |
| [[Events.CityDefenseStatusChanged]] | `playerID [number]`<br/>`iValue [number]` |
| [[Events.CityFocusChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[Events.CityInitialized]] | `playerID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[Events.CityLiberated]] | `playerID [number]`<br/>`cityID [number]` |
| [[Events.CityLoyaltyChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[Events.CityMadePurchase]] | `playerID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`purchaseType [number]`<br/>`objectType [number]` |
| [[Events.CityNameChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[Events.CityOccupationChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[Events.CityPopulationChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`cityPopulation [number]` |
| [[Events.CityProductionChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`productionID [number]`<br/>`objectID [number]`<br/>`bCancelled [boolean]` |
| [[Events.CityProductionCompleted]] | `playerID [number]`<br/>`cityID [number]`<br/>`iConstructionType [number]`<br/>`unitID [number]`<br/>`bCancelled [boolean]` |
| [[Events.CityProductionUpdated]] | `playerID [number]`<br/>`cityID [number]`<br/>`objectID [number]`<br/>`productionID [number]` |
| [[Events.CityProjectCompleted]] | `playerID [number]`<br/>`cityID [number]`<br/>`projectID [number]`<br/>`buildingIndex [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`bCancelled [boolean]` |
| [[Events.CityReligionChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`eVisibility [number]`<br/>`city` |
| [[Events.CityReligionFollowersChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`eVisibility [number]`<br/>`city` |
| [[Events.CityRemovedFromMap]] | `playerID [number]`<br/>`cityID [number]` |
| [[Events.CitySiegeStatusChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`bIsBesieged [boolean]` |
| [[Events.CityTileOwnershipChanged]] | `owner [number]`<br/>`cityID [number]` |
| [[Events.CityTransfered]] | `playerID [number]`<br/>`cityID [number]` |
| [[Events.CityUnitsChanged]] | `playerID [number]`<br/>`cityID [number]` |
| [[Events.CityVisibilityChanged]] | `playerID [number]`<br/>`cityID [number]`<br/>`eVisibility [number]` |
| [[Events.CityWorkerChanged]] | `ownerPlayerID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[Events.CivicBoostTriggered]] | `playerID [number]`<br/>`iBoostedCivic [number]`<br/>`iUnknownA [number]`<br/>`iUnknownB [number]` |
| [[Events.CivicChanged]] | `ePlayer [number]`<br/>`eCivic [number]` |
| [[Events.CivicCompleted]] | `playerID [number]`<br/>`iCivic [number]`<br/>`bCancelled [boolean]` |
| [[Events.CivicQueueChanged]] |  |
| [[Events.CivicsUnlocked]] |  |
| [[Events.CliffAddedToMap]] |  |
| [[Events.CliffRemovedFromMap]] |  |
| [[Events.Combat]] | `combatResult [table]` |
| [[Events.CulturalIdentityCitizenConverted]] |  |
| [[Events.CulturalIdentityCityConverted]] | `player [number]`<br/>`cityID [number]`<br/>`fromPlayer [number]` |
| [[Events.CulturalIdentityConversionOutcomeChanged]] | `player [number]`<br/>`cityID [number]`<br/>`eOutcome [number]` |
| [[Events.CultureChanged]] |  |
| [[Events.CultureYieldChanged]] | `ePlayer [number]` |
| [[Events.DiplomacyDealEnacted]] |  |
| [[Events.DiplomacyDealExpired]] |  |
| [[Events.DiplomacyDeclareWar]] | `firstPlayerID [number]`<br/>`secondPlayerID [number]` |
| [[Events.DiplomacyIncomingDeal]] | `eFromPlayer [number]`<br/>`eToPlayer [number]`<br/>`eAction [number]` |
| [[Events.DiplomacyMakePeace]] | `firstPlayerID [number]`<br/>`secondPlayerID [number]` |
| [[Events.DiplomacyMeet]] | `player1ID [number]`<br/>`player2ID [number]` |
| [[Events.DiplomacyMeetMajorMinor]] |  |
| [[Events.DiplomacyMeetMajors]] |  |
| [[Events.DiplomacyRefusePeace]] | `eActingPlayer [number]`<br/>`eReactingPlayer [number]` |
| [[Events.DiplomacyRelationshipChanged]] | `player1ID [number]`<br/>`player2ID [number]` |
| [[Events.DiplomacySessionClosed]] | `sessionID [number]` |
| [[Events.DiplomacyStatement]] | `eActingPlayer [number]`<br/>`eReactingPlayer [number]`<br/>`values [table]` |
| [[Events.DistrictAddedToMap]] | `playerID [number]`<br/>`districtID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`districtType [number]`<br/>`percentComplete [number]` |
| [[Events.DistrictBuildingRestore]] |  |
| [[Events.DistrictBuildProgressChanged]] | `playerID [number]`<br/>`districtID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`districtType [number]`<br/>`era [number]`<br/>`civilization [number]`<br/>`percentComplete [number]`<br/>`iAppeal [number]`<br/>`isPillaged [number]` |
| [[Events.DistrictCombatChanged]] | `eventSubType [number]`<br/>`playerID [number]`<br/>`districtID [number]` |
| [[Events.DistrictDamageChanged]] | `playerID [number]`<br/>`districtID [number]`<br/>`damageType [number]`<br/>`newDamage [number]`<br/>`oldDamage [number]` |
| [[Events.DistrictPillaged]] | `owner [number]`<br/>`districtID [number]`<br/>`cityID [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`districtType [number]`<br/>`percentComplete [number]`<br/>`isPillaged [number]` |
| [[Events.DistrictRemovedFromMap]] | `playerID [number]`<br/>`districtID [number]` |
| [[Events.DistrictUnitsChanged]] | `playerID [number]`<br/>`districtID [number]` |
| [[Events.DistrictVisibilityChanged]] | `playerID [number]`<br/>`districtID [number]`<br/>`eVisibility [number]` |
| [[Events.EmergenciesUpdated]] |  |
| [[Events.EmergencyAvailable]] | `playerTarget [number]`<br/>`emergencyType [number]` |
| [[Events.EmergencyAvailableParticipant]] |  |
| [[Events.EmergencyCompleted]] | `playerID [number]`<br/>`eTargetPlayer [number]`<br/>`iTurn [number]` |
| [[Events.EmergencyCompleteParticipants]] |  |
| [[Events.EmergencyRejected]] |  |
| [[Events.EmergencyStarted]] | `playerID [number]`<br/>`eTargetPlayer [number]`<br/>`iTurn [number]` |
| [[Events.EndTurnBlockingChanged]] | `ePrevEndTurnBlockingType [number]`<br/>`eNewEndTurnBlockingType [number]` |
| [[Events.EndTurnDirty]] |  |
| [[Events.EndWonderReveal]] |  |
| [[Events.EventPopupRequest]] |  |
| [[Events.EventSoundRequest]] |  |
| [[Events.FaithChanged]] | `playerID [number]`<br/>`yield [number]`<br/>`balance [number]` |
| [[Events.FeatureAddedToMap]] |  |
| [[Events.FeatureChanged]] |  |
| [[Events.FeatureRemovedFromMap]] |  |
| [[Events.FeatureVisibilityChanged]] |  |
| [[Events.GameEraChanged]] | `previousEra [number]`<br/>`newEra [number]` |
| [[Events.GameHistoryMomentRecorded]] | `momentIndex [number]`<br/>`iUnknown [number]` |
| [[Events.GoodyHutReward]] | `playerID [number]`<br/>`unitID [number]`<br/>`iUnknown1 [number]`<br/>`iUnknown2 [number]` |
| [[Events.GovDistrictPolicyLocked]] |  |
| [[Events.GovDistrictPolicyUnlocked]] | `player [number]`<br/>`policyType [number]` |
| [[Events.GovernmentChanged]] | `playerID [number]`<br/>`governmentID [number]` |
| [[Events.GovernmentPolicyChanged]] | `playerID [number]`<br/>`policyID [number]` |
| [[Events.GovernmentPolicyObsoleted]] | `ePlayer [number]` |
| [[Events.GovernorAppointed]] | `playerID [number]`<br/>`governorID [number]` |
| [[Events.GovernorAssigned]] | `cityOwner [number]`<br/>`cityID [number]`<br/>`governorOwner [number]`<br/>`governorType [number]` |
| [[Events.GovernorChanged]] | `playerID [number]`<br/>`governorID [number]` |
| [[Events.GovernorEstablished]] |  |
| [[Events.GovernorPointsChanged]] | `player [number]`<br/>`iDelta [number]` |
| [[Events.GovernorPromoted]] | `ePlayer [number]`<br/>`eGovernor [number]`<br/>`ePromotion [number]` |
| [[Events.GreatPeoplePointsChanged]] | `playerID [number]` |
| [[Events.GreatPeopleTimelineChanged]] |  |
| [[Events.GreatWorkCreated]] | `playerID [number]`<br/>`unitID [number]`<br/>`iCityPlotX [number]`<br/>`iCityPlotY [number]`<br/>`buildingID [number]`<br/>`greatWorkID [number]` |
| [[Events.GreatWorkMoved]] | `fromCityOwner [number]`<br/>`fromCityID [number]`<br/>`toCityOwner [number]`<br/>`toCityID [number]`<br/>`buildingID [number]`<br/>`greatWorkType [number]` |
| [[Events.ImprovementActivated]] | `iX [number]`<br/>`iY [number]`<br/>`unitOwner [number]`<br/>`unitID [number]`<br/>`improvementType [number]`<br/>`improvementOwner [number]`<br/>`activationType [number]` |
| [[Events.ImprovementAddedToMap]] | `iX [number]`<br/>`iY [number]`<br/>`eImprovement [number]`<br/>`playerID [number]` |
| [[Events.ImprovementChanged]] | `iX [number]`<br/>`iY [number]`<br/>`improvementType [number]`<br/>`improvementOwner [number]`<br/>`resource [number]`<br/>`isPillaged [boolean]`<br/>`isWorked [boolean]` |
| [[Events.ImprovementOwnershipChanged]] |  |
| [[Events.ImprovementRemovedFromMap]] | `iX [number]`<br/>`iY [number]`<br/>`eOwner [number]` |
| [[Events.ImprovementVisibilityChanged]] | `iX [number]`<br/>`iY [number]`<br/>`eImprovementType [number]`<br/>`eVisibility [number]` |
| [[Events.InfluenceChanged]] |  |
| [[Events.InfluenceGiven]] | `citystateID [number]`<br/>`playerID [number]` |
| [[Events.LevyCounterChanged]] | `originalOwnerID [number]` |
| [[Events.LocalPlayerChanged]] | `localPlayerID [number]`<br/>`prevLocalPlayerID [number]` |
| [[Events.LocalPlayerTurnBegin]] |  |
| [[Events.LocalPlayerTurnEnd]] |  |
| [[Events.LocalPlayerTurnUnready]] |  |
| [[Events.MapYieldsChanged]] |  |
| [[Events.NationalParkAdded]] |  |
| [[Events.NationalParkRemoved]] |  |
| [[Events.NationalParkVisibilityChanged]] |  |
| [[Events.NaturalWonderRevealed]] | `iX [number]`<br/>`iY [number]`<br/>`eFeature [number]`<br/>`bIsFirstToFind [boolean]` |
| [[Events.NotificationActivated]] | `playerID [number]`<br/>`notificationID [number]`<br/>`bActivatedByUser [boolean]` |
| [[Events.NotificationAdded]] | `playerID [number]`<br/>`notificationID [number]` |
| [[Events.NotificationDismissed]] | `playerID [number]`<br/>`notificationID [number]` |
| [[Events.NotificationRefreshRequested]] |  |
| [[Events.ObjectPairing]] | `eSubType [number]`<br/>`parentOwner [number]`<br/>`parentType [number]`<br/>`parentID [number]`<br/>`childOwner [number]`<br/>`childType [number]`<br/>`childID [number]` |
| [[Events.OnAiAdvisorUpdated]] |  |
| [[Events.UnitGreatPersonActivated]] | `unitOwner [number]`<br/>`unitID [number]`<br/>`greatPersonClassID [number]`<br/>`greatPersonIndividualID [number]`<br/>`unitOwner [number]`<br/>`unitID [number]`<br/>`greatPersonClassID [number]`<br/>`greatPersonIndividualID [number]` |
| [[Events.PantheonFounded]] | `ePlayer [number]` |
| [[Events.PhaseBegin]] |  |
| [[Events.PhaseEnd]] |  |
| [[Events.PlayerAgeChanged]] | `playerID [number]` |
| [[Events.PlayerBordersChanged]] |  |
| [[Events.PlayerDarkAgeChanged]] | `playerID [number]` |
| [[Events.PlayerDefeat]] | `playerID [number]`<br/>`defeatType [number]`<br/>`eventID [number]` |
| [[Events.PlayerDestroyed]] |  |
| [[Events.PlayerEraChanged]] | `playerID [number]`<br/>`eraID [number]` |
| [[Events.PlayerEraScoreChanged]] | `playerID [number]`<br/>`amountAwarded [number]` |
| [[Events.PlayerEraTransitionBegins]] | `playerID [number]` |
| [[Events.PlayerOperationComplete]] |  |
| [[Events.PlayerResourceChanged]] | `ownerPlayerID [number]`<br/>`resourceTypeID [number]` |
| [[Events.PlayerRestored]] |  |
| [[Events.PlayerRevived]] |  |
| [[Events.PlayerTurnActivated]] | `playerID [number]`<br/>`bIsFirstTime [boolean]` |
| [[Events.PlayerTurnDeactivated]] | `playerID [number]` |
| [[Events.PlayerVictory]] |  |
| [[Events.PlotAppealChanged]] |  |
| [[Events.PlotMarkerChanged]] | `iX [number]`<br/>`iY [number]` |
| [[Events.PlotVisibilityChanged]] | `iX [number]`<br/>`iY [number]`<br/>`visibilityType [number]` |
| [[Events.PlotYieldChanged]] | `iX [number]`<br/>`iY [number]` |
| [[Events.QuestChanged]] | `CityStateID [number]`<br/>`CompletedQuestPlayerID [number]` |
| [[Events.QueueFlushed]] |  |
| [[Events.ReligionFounded]] | `playerID [number]`<br/>`religionID [number]` |
| [[Events.RemotePlayerTurnBegin]] |  |
| [[Events.RemotePlayerTurnEnd]] |  |
| [[Events.RemotePlayerTurnUnready]] |  |
| [[Events.ResearchChanged]] | `ePlayer [number]`<br/>`eTech [number]` |
| [[Events.ResearchCompleted]] | `ePlayer [number]`<br/>`eTech [number]` |
| [[Events.ResearchQueueChanged]] | `ePlayer [number]`<br/>`eTech [number]` |
| [[Events.ResearchYieldChanged]] | `ePlayer [number]` |
| [[Events.ResourceAddedToMap]] | `iX [number]`<br/>`iY [number]`<br/>`resourceType [number]` |
| [[Events.ResourceChanged]] |  |
| [[Events.ResourceRemovedFromMap]] | `iX [number]`<br/>`iY [number]`<br/>`resourceType [number]` |
| [[Events.ResourceVisibilityChanged]] | `iX [number]`<br/>`iY [number]`<br/>`resourceType [number]`<br/>`visibilityType [number]` |
| [[Events.RiverAddedToMap]] |  |
| [[Events.RiverRemovedFromMap]] |  |
| [[Events.RouteAddedToMap]] |  |
| [[Events.RouteChanged]] | `iX [number]`<br/>`iY [number]` |
| [[Events.RouteRemovedFromMap]] |  |
| [[Events.RouteVisibilityChanged]] |  |
| [[Events.SpyAdded]] | `spyOwner [number]`<br/>`spyUnitID [number]` |
| [[Events.SpyMissionCompleted]] | `playerID [number]`<br/>`missionID [number]` |
| [[Events.SpyMissionUpdated]] |  |
| [[Events.SpyRemoved]] | `spyOwner [number]`<br/>`counterSpyPlayer [number]` |
| [[Events.SpyUpdated]] |  |
| [[Events.StatusMessage]] |  |
| [[Events.SystemUpdateUI]] | `type [number]`<br/>`tag [string]`<br/>`iData1 [number]`<br/>`iData2 [number]`<br/>`strData1 [string]` |
| [[Events.TeamVictory]] |  |
| [[Events.TechBoostTriggered]] | `playerID [number]`<br/>`iTechBoosted [number]`<br/>`iUnknownA [number]`<br/>`iUnknownB [number]` |
| [[Events.TerrainTypeChanged]] |  |
| [[Events.TradeRouteActivityChanged]] | `playerID [number]`<br/>`OriginPlayerID [number]`<br/>`OriginCityID [number]`<br/>`TargetPlayerID [number]`<br/>`TargetCityID [number]` |
| [[Events.TradeRouteAddedToMap]] | `playerID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[Events.TradeRouteCapacityChanged]] | `playerID [number]` |
| [[Events.TradeRouteRangeChanged]] |  |
| [[Events.TradeRouteRemovedFromMap]] | `playerID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[Events.TreasuryChanged]] | `playerID [number]`<br/>`yield [number]`<br/>`balance [number]` |
| [[Events.TurnBegin]] |  |
| [[Events.TurnEnd]] |  |
| [[Events.UnitAbilityGained]] | `playerID [number]`<br/>`unitID [number]`<br/>`eAbilityType [number]` |
| [[Events.UnitActivate]] |  |
| [[Events.UnitActivityChanged]] | `playerID [number]`<br/>`unitID [number]`<br/>`eActivityType [number]` |
| [[Events.UnitAirlifted]] |  |
| [[Events.UnitArtifactChanged]] | `playerID [number]`<br/>`unitID [number]` |
| [[Events.UnitCaptured]] | `currentUnitOwner [number]`<br/>`unitID [number]`<br/>`owningPlayer [number]`<br/>`capturingPlayer [number]` |
| [[Events.UnitChargesChanged]] | `playerID [number]`<br/>`unitID [number]`<br/>`newCharges [number]`<br/>`oldCharges [number]` |
| [[Events.UnitCommandStarted]] | `playerID [number]`<br/>`unitID [number]`<br/>`hCommand [number]`<br/>`iData1 [number]` |
| [[Events.UnitDamageChanged]] | `PlayerID [number]`<br/>`UnitID [number]`<br/>`newDamage [number]`<br/>`prevDamage [number]` |
| [[Events.UnitEmbarkedStateChanged]] | `playerID [number]`<br/>`unitID [number]`<br/>`bEmbarkedState [boolean]` |
| [[Events.UnitEnterFormation]] | `firstUnitOwner [number]`<br/>`firstUnitID [number]`<br/>`secondUnitOwner [number]`<br/>`secondUnitID [number]` |
| [[Events.UnitExitFormation]] | `firstUnitOwner [number]`<br/>`firstUnitID [number]`<br/>`secondUnitOwner [number]`<br/>`secondUnitID [number]` |
| [[Events.UnitExperienceChanged]] |  |
| [[Events.UnitFormArmy]] | `playerID [number]`<br/>`unitID [number]` |
| [[Events.UnitFormationChanged]] |  |
| [[Events.UnitFormCorps]] | `playerID [number]`<br/>`unitID [number]` |
| [[Events.UnitFortificationChanged]] | `playerID [number]`<br/>`unitID [number]` |
| [[Events.UnitGreatPersonChanged]] |  |
| [[Events.UnitGreatPersonCreated]] | `playerID [number]`<br/>`unitID [number]`<br/>`greatPersonClassID [number]`<br/>`greatPersonIndividualID [number]` |
| [[Events.UnitKilledInCombat]] | `killedPlayerID [number]`<br/>`killedUnitID [number]`<br/>`playerID [number]`<br/>`unitID [number]` |
| [[Events.UnitMoveComplete]] | `playerID [number]`<br/>`unitID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[Events.UnitMoved]] | `playerID [number]`<br/>`unitID [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`locallyVisible`<br/>`stateChange` |
| [[Events.UnitMovementPointsChanged]] | `playerID [number]`<br/>`unitID [number]`<br/>`MovementPoints [number]` |
| [[Events.UnitMovementPointsCleared]] | `playerID [number]`<br/>`unitID [number]` |
| [[Events.UnitMovementPointsRestored]] | `playerID [number]`<br/>`unitID [number]`<br/>`MovementPoints [number]` |
| [[Events.UnitOperationAdded]] | `playerID [number]`<br/>`unitID [number]`<br/>`iUnknown [number]`<br/>`hOperation [number]` |
| [[Events.UnitOperationDeactivated]] | `playerID [number]`<br/>`unitID [number]`<br/>`hOperation [number]`<br/>`iData1 [number]` |
| [[Events.UnitOperationSegmentComplete]] | `playerID [number]`<br/>`unitID [number]`<br/>`hCommand [number]`<br/>`iData1 [number]` |
| [[Events.UnitOperationStarted]] | `ownerID [number]`<br/>`unitID [number]`<br/>`operationID [number]` |
| [[Events.UnitOperationsCleared]] | `playerID [number]`<br/>`unitID [number]`<br/>`hCommand [number]`<br/>`iData1 [number]` |
| [[Events.UnitParadropped]] |  |
| [[Events.UnitPromoted]] | `playerID [number]`<br/>`unitID [number]` |
| [[Events.UnitPromotionAvailable]] | `playerID [number]`<br/>`unitID [number]`<br/>`promotionID [number]` |
| [[Events.UnitRemovedFromMap]] | `playerID [number]`<br/>`unitID [number]` |
| [[Events.UnitTeleported]] | `playerID [number]`<br/>`unitID [number]`<br/>`iX [number]`<br/>`iY [number]` |
| [[Events.UnitTradeChanged]] | `playerID [number]`<br/>`unitID [number]` |
| [[Events.UnitUpgraded]] | `playerID [number]`<br/>`unitID [number]` |
| [[Events.UnitVisibilityChanged]] | `playerID [number]`<br/>`unitID [number]` |
| [[Events.WMDCountChanged]] | `playerID [number]`<br/>`eWMD [number]` |
| [[Events.WMDDetonated]] |  |
| [[Events.WMDFalloutChanged]] |  |
| [[Events.WMDFalloutVisibilityChanged]] |  |
| [[Events.WonderCompleted]] | `iX [number]`<br/>`iY [number]`<br/>`buildingIndex [number]`<br/>`playerIndex [number]`<br/>`cityID [number]`<br/>`iPercentComplete [number]`<br/>`iUnknown [number]` |
| [[Events.WorldTextMessage]] | `messageType [number]`<br/>`delay [number]`<br/>`iX [number]`<br/>`iY [number]`<br/>`text [number]` |
