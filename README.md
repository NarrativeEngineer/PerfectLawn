# Perfect Lawn
Aronelle's Spick and Span Lawn

# Lawn & Order - Game Design Document

## 🎯 Game Overview
- **Title:** Lawn & Order (working title)
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
| 4     | Norman (cigarette butts)              | Medium-High   |
| 5     | Combo (birds, trash, Norman, dandelion)| High          |

## 👥 Characters & Threats

| Character          | Behavior                          | Action Required     |
|-------------------|-----------------------------------|---------------------|
| Neighbour          | Walks by and comments             | None (goal outcome) |
| Bird               | Lands and poops                   | Yell into mic       |
| Ant                | Builds nest                       | Tap to squash       |
| Norman             | Flicks cigarette butts            | Tap before flick    |
| Kid                | Throws trash                      | Swipe to deflect    |
| Dog                | Attempts to pee                   | Hose or redirect    |
| Teen Driver        | Skids on lawn                     | Tap obstacle trap   |
| Distracted Shopper | Leaves trolley on lawn            | Swipe away          |

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
---

*“Make your patch the envy of the suburb.”*

