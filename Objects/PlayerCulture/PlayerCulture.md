# PlayerCulture
## Instance
This file is a description of an Instance’s Metatable. There is no accessible variable of this name. Most of its methods will expect an implicit "self" argument and should be invoked with a `:`.

## Methods
| Script | UI  |                Returns | . or : | Name                                                                                     | Arguments               |
|:------:|:---:| ----------------------:|:------ |:---------------------------------------------------------------------------------------- |:----------------------- |
|        |  ✓  |                        | :      | [[PlayerCulture.CanChangeGovernment\|CanChangeGovernment]]                               |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.CanChangeGovernmentAtAll\|CanChangeGovernmentAtAll]]                     |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.CanPolicyBeSlotted\|CanPolicyBeSlotted]]                                 |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.CanProgress\|CanProgress]]                                               |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.CanSlotPolicy\|CanSlotPolicy]]                                           |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.CanTriggerBoost\|CanTriggerBoost]]                                       |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.ChangeCurrentCulturalProgress\|ChangeCurrentCulturalProgress]]           |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.CivicCompletedThisTurn\|CivicCompletedThisTurn]]                         |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.CivicUnlocksGovernment\|CivicUnlocksGovernment]]                         |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.ClearPolicySlot\|ClearPolicySlot]]                                       |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetAnarchyEndTurn\|GetAnarchyEndTurn]]                                   |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.GetAnarchyTurns\|GetAnarchyTurns]]                                       |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetAutoThemedBuilding\|GetAutoThemedBuilding]]                           |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.GetCivicCompletedThisTurn\|GetCivicCompletedThisTurn]]                   |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetCivicPath\|GetCivicPath]]                                             |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetCivicQueue\|GetCivicQueue]]                                           |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetCostToUnlockPolicies\|GetCostToUnlockPolicies]]                       |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetCulturalProgress\|GetCulturalProgress]]                               |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.GetCultureCost\|GetCultureCost]]                                         |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.GetCultureYield\|GetCultureYield]]                                       |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetCultureYieldToolTip\|GetCultureYieldToolTip]]                         |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetCurrentGovernment\|GetCurrentGovernment]]                             |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetEnactPolicyCost\|GetEnactPolicyCost]]                                 |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetExtraTradeRouteTourismModifier\|GetExtraTradeRouteTourismModifier]]   |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetFlatBonus\|GetFlatBonus]]                                             |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetGreatWorksInCity\|GetGreatWorksInCity]]                               |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetIncrementingBonus\|GetIncrementingBonus]]                             |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetIncrementingBonusIncrement\|GetIncrementingBonusIncrement]]           |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetIncrementingBonusInterval\|GetIncrementingBonusInterval]]             |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetIncrementingBonusTurnsUntilNext\|GetIncrementingBonusTurnsUntilNext]] |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetLifetimeCulture\|GetLifetimeCulture]]                                 |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetNumPoliciesUnlocked\|GetNumPoliciesUnlocked]]                         |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.GetNumPolicySlots\|GetNumPolicySlots]]                                   |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetNumPolicySlotsOpen\|GetNumPolicySlotsOpen]]                           |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.GetPolicyToUnlock\|GetPolicyToUnlock]]                                   |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.GetProgressingCivic\|GetProgressingCivic]]                               |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.GetSlotPolicy\|GetSlotPolicy]]                                           |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetSlotType\|GetSlotType]]                                               |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetStaycationers\|GetStaycationers]]                                     |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetTourismAt\|GetTourismAt]]                                             |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetTourismTooltipAt\|GetTourismTooltipAt]]                               |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetTouristsAt\|GetTouristsAt]]                                           |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetTouristsFrom\|GetTouristsFrom]]                                       |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetTouristsFromTooltip\|GetTouristsFromTooltip]]                         |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetTouristsTo\|GetTouristsTo]]                                           |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetTurnsLeft\|GetTurnsLeft]]                                             |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.GetTurnsLeftOnCurrentCivic\|GetTurnsLeftOnCurrentCivic]]                 |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetTurnsToProgressCivic\|GetTurnsToProgressCivic]]                       |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetTurnsUntilDominant\|GetTurnsUntilDominant]]                           |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GetTurnsUntilVictory\|GetTurnsUntilVictory]]                             |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GovernmentChangeConsidered\|GovernmentChangeConsidered]]                 |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.GovernmentChangeMade\|GovernmentChangeMade]]                             |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.HasBoostBeenTriggered\|HasBoostBeenTriggered]]                           |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.HasCivic\|HasCivic]]                                                     |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.IsAutoThemedEligible\|IsAutoThemedEligible]]                             |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.IsCivicRevealed\|IsCivicRevealed]]                                       |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.IsEverAutoThemable\|IsEverAutoThemable]]                                 |                         |
|   ✓    |  ✓  | `IsUnlocked [boolean]` | :      | [[PlayerCulture.IsGovernmentUnlocked\|IsGovernmentUnlocked]]                             | `GovernmentID [number]` |
|        |  ✓  |                        | :      | [[PlayerCulture.IsInAnarchy\|IsInAnarchy]]                                               |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.IsPolicyActive\|IsPolicyActive]]                                         |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.IsPolicyBanned\|IsPolicyBanned]]                                         |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.IsPolicyObsolete\|IsPolicyObsolete]]                                     |                         |
|   ✓    |  ✓  |                        | :      | [[PlayerCulture.IsPolicyUnlocked\|IsPolicyUnlocked]]                                     |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.PolicyChangeMade\|PolicyChangeMade]]                                     |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.RequestChangeGovernment\|RequestChangeGovernment]]                       |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.RequestClearSlot\|RequestClearSlot]]                                     |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.RequestEnactPolicy\|RequestEnactPolicy]]                                 |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.RequestPolicyChanges\|RequestPolicyChanges]]                             |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.ReverseBoost\|ReverseBoost]]                                             |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.SetCivic\|SetCivic]]                                                     |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.SetCivicCompletedThisTurn\|SetCivicCompletedThisTurn]]                   |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.SetCulturalProgress\|SetCulturalProgress]]                               |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.SetCurrentGovernment\|SetCurrentGovernment]]                             |                         |
|        |  ✓  |                        | :      | [[PlayerCulture.SetGovernmentChangeConsidered\|SetGovernmentChangeConsidered]]           |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.SetProgressingCivic\|SetProgressingCivic]]                               |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.TriggerBoost\|TriggerBoost]]                                             |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.UnlockGovernment\|UnlockGovernment]]                                     |                         |
|   ✓    |     |                        | :      | [[PlayerCulture.UnlockPolicy\|UnlockPolicy]]                                             |                         |
