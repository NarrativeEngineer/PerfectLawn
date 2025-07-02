# Perfect Lawn
Aronelle's Spick and Span Lawn

=======
This repository contains the configuration for the mobile game "Perfect Lawn". See `game_config.py` for gameplay details.

# Perfect Lawn - Game Design Document

## 🎯 Game Overview
- **Title:** Perfect Lawn
- **Genre:** Casual Defense / Comedy Simulation
- **Platform:** Mobile (iOS, Android)
- **Audience:** Ages 10+, fans of humor and casual strategy

## 🌿 Game Objective
Protect your lawn from an increasing barrage of weeds, pests, and unruly visitors. Success means hearing delightful praise from your nosy elderly neighbours. Failure leads to their tutting disapproval!

## 🕹️ Core Mechanics

### Input Methods
- **Blow into Microphone** – Clear dandelion seeds
- **Yell into Microphone** – Scare off pooping birds
- **Tap** – Eliminate ants, wasps, pests
- **Swipe/Drag** – Remove trash, trolleys, dogs
- **Hold + Swipe** – Hose down messes
- **Tap Timing** – Stop Norman before flicking cigarette butts

### Lawn Health Meter
- Tracks how clean your lawn is
- Depletes with missed actions
- Refills slightly when threats are cleared

## 📈 Level Design

### Tutorial (Level 0)
- Focus: Teaching mic-blow mechanic
- Threat: Floating dandelion seeds

### Sample Levels

| Level | New Threats Introduced                | Complexity    |
|-------|----------------------------------------|---------------|
| 1     | Dandelion seeds                        | Low           |
| 2     | Birds (pooping)                        | Low           |
| 3     | Kids throwing trash                    | Medium        |
| 4     | Norman (cigarette butts)               | Medium-High   |
| 5     | Combo (birds, trash, Norman, dandelion)| High          |

## 👥 Characters & Threats

| Character          | Behavior                          | Action Required     |
|-------------------|-----------------------------------|---------------------|
| Neighbour (Norm & Brigitta) | Walks by and comments             | None (goal outcome) |
| Birds (Aussie fauna) | Lands and poops                   | Yell into mic       |
| Ant                | Builds nest                       | Tap to squash       |
| Norman             | Flicks cigarette butts            | Tap before flick    |
| Kid                | Throws trash                      | Swipe to deflect    |
| Dog                | Attempts to pee                   | Hose or redirect    |
| Teen Driver        | Skids on lawn                     | Tap obstacle trap   |
| Distracted Shopper | Leaves trolley on lawn            | Swipe away          |


### Birdwatch Badges

| Bird Species | Rarity | Badge Unlock |
| ------------ | ------ | ------------ |
| Bin chicken | Common | On first sighting |
| Cockatoo | Rare | On first sighting |
| Rock pigeons | Common | On first sighting |
| Sea gulls | Medium rare | On first sighting |
| Budgies | Rare | On first sighting |
| Rainbow lorikeet | Rare | On first sighting |
| Black cockatoo | Rarest | On first sighting |
| Black swan | Rarest | On first sighting |
Bird species appear randomly at higher levels, unlocking a new badge when spotted.

## 🔊 Audio

- **Mic input detection:** blow, yell
- **SFX:** wind, poop splat, hose spray, crunches
- **Voice Lines:** neighbour praise/criticism
- **Background:** garden ambience

## 🎨 Visual Design

- Stylized cartoon visuals
- Central lawn as play zone
- UI elements: health bar, mic status, threat icons
- Character animations

## 🧭 UI Elements

- Start/Pause/Settings
- Compliment Meter
- Mic input indicator
- End-of-level review: “Neighbour Feedback”

## 📚 Progression

- Each level increases speed and number of threats
- Threats overlap for complexity
- Optional bonus stages (e.g. nighttime lawn, storm weather)

## 🈵 Success

- when you receive 5 compliments by Norman or Brigitta you receive the Lawn Domination badge
=======
- Bird species unlock badges when spotted during higher levels
- Optional bonus stages (e.g. nighttime lawn, storm weather)
---

*“Make your patch the envy of the suburb.”*
=======
## Level Escalation Plan

The game introduces threats gradually across 16 levels.

| Level | Focus                                     |
| ----- | ----------------------------------------- |
| 0     | Tutorial: blow away dandelion seeds       |
| 1     | Faster dandelion seeds                    |
| 2     | Birds drop poop—yell to scare them        |
| 3     | Tap ants before they nest                 |
| 4     | Swipe to clear kid-thrown trash           |
| 5     | Stop Norman's cigarette flicks            |
| 6     | Birds and seeds overlap                   |
| 7     | Norman and kids require tap and swipe     |
| 8     | Ants, trash and seeds demand multitasking |
| 9     | Dogs appear, introducing hose mechanic    |
| 10    | Mix Norman, birds and dogs                |
| 11    | Teen drivers leave skid marks             |
| 12    | Shoppers' trolleys plus mid-air threats   |
| 13    | Wasps require rapid taps                  |
| 14    | All previous threats speed up             |
| 15    | Boss wave with every threat               |

Later levels continue to combine earlier challenges, increasing threat speed and frequency.

## Zen Relaxation Levels

Between major sections, players can unwind in special "Zen" stages that offer gentle tasks and rewards.

| Zen Level | Theme                    | Activities                           | Rewards                          |
| --------- | ----------------------- | ------------------------------------ | -------------------------------- |
| 10Z       | Tea Garden              | Rake leaves, place lanterns          | +Lawn Health Boost (next 3 lvls) |
| 20Z       | Mini Pond               | Place koi fish, skim floating petals | +Auto-hose for dog pee (temp)    |
| 30Z       | Bonsai Courtyard        | Trim trees, arrange stones           | Norman flick delay +1s (next 5)  |
| 40Z       | Sakura Garden           | Catch petals, arrange benches        | Reduce trash rate by 20%         |
| 50Z       | Zen Sand Raking Mastery | Freeform rake art, candle lighting   | Unlock permanent décor pieces    |
\nFor asset and inspiration credits, see [CREDITS.md](CREDITS.md)
