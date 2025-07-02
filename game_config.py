# Game Requirements for Perfect Lawn

# 1. Game Metadata
game = {
    "title": "Perfect Lawn",
    "genre": "Casual Defense / Comedy Simulation",
    "platform": ["iOS", "Android"],
    "audience": "Ages 10+",
    "summary": "Protect your lawn from weeds, pests, and unruly neighbors to earn praise."
}

# 2. Player Input Mechanisms
input_mechanics = {
    "microphone": [
        {"action": "blow", "effect": "remove dandelion seeds"},
        {"action": "yell", "effect": "scare birds"}
    ],
    "tap": "squash bugs or pests",
    "swipe": "flick trash or move trolleys",
    "hold_swipe": "hose messes",
    "quick_tap": "target and prevent Norman's littering"
}

# 3. Lawn Health System
lawn_health = {
    "meter": "Neighbour Compliment Meter",
    "depletion_events": ["missed threats", "delayed responses"],
    "replenish_events": ["successful actions", "level completions"]
}

# 4. Level Design
levels = [
    {"level": 0, "threats": ["dandelion seeds"],
        "notes": "Tutorial: learn to blow into the mic"},
    {"level": 1, "threats": ["dandelion seeds"],
        "notes": "Faster seeds for timing practice"},
    {"level": 2, "threats": ["birds"],
        "notes": "Yell to scare poop-dropping birds"},
    {"level": 3, "threats": ["ants"],
        "notes": "Tap nests quickly"},
    {"level": 4, "threats": ["kids"],
        "notes": "Swipe trash accurately"},
    {"level": 5, "threats": ["Norman"],
        "notes": "Quick taps to stop littering"},
    {"level": 6, "threats": ["birds", "dandelion seeds"],
        "notes": "Overlapping mic actions"},
    {"level": 7, "threats": ["Norman", "kids"],
        "notes": "Tap and swipe simultaneously"},
    {"level": 8, "threats": ["ants", "trash", "dandelion seeds"],
        "notes": "Multitask across the field"},
    {"level": 9, "threats": ["dogs"],
        "notes": "Introduce hose/sustained swipe"},
    {"level": 10, "threats": ["Norman", "birds", "dogs"],
        "notes": "Mic, tap and swipe combos"},
    {"level": 11, "threats": ["teen drivers"],
        "notes": "Block burnouts with quick taps"},
    {"level": 12, "threats": ["shoppers"],
        "notes": "Swipe trolleys while juggling birds"},
    {"level": 13, "threats": ["wasps"],
        "notes": "Rapid taps to stop hive buildup"},
    {"level": 14, "threats": ["mixed"],
        "notes": "All prior threats appear faster"},
    {"level": 15, "threats": ["boss mix"],
        "notes": "Survive every threat for 90 seconds"}
]

# Detailed bird species with rarity for birdwatch badges

bird_types = [
    {"name": "bin chicken", "rarity": "common"},
    {"name": "cockatoo", "rarity": "rare"},
    {"name": "rock pigeons", "rarity": "common"},
    {"name": "sea gulls", "rarity": "medium rare"},
    {"name": "budgies", "rarity": "rare"},
    {"name": "rainbow lorikeet", "rarity": "rare"},
    {"name": "black cockatoo", "rarity": "rarest"},
    {"name": "black swan", "rarity": "rarest"},
]

# Track which birdwatch badges the player has unlocked

birdwatch_badges = {
    "bin chicken": False,
    "cockatoo": False,
    "rock pigeons": False,
    "sea gulls": False,
    "budgies": False,
    "rainbow lorikeet": False,
    "black cockatoo": False,
    "black swan": False,
}

# 5. Characters and Behaviors
characters = {
    "Elderly Neighbours": "Norm and Brigitta give praise or disapproval",
    "Bird": "Poops on lawn unless scared",
    "Ant": "Attempts to nest, tap to squash",
    "Norman": "Flicks cigarette butts unless tapped quickly",
    "Kid": "Throws trash, swipe to flick back",
    "Dog": "Pees unless redirected",
    "Teen Driver": "Leaves skid marks",
    "Shopper": "Leaves trolley, swipe to remove"
}

# 6. Audio Requirements
audio = {
    "input_detection": ["blow", "yell"],
    "effects": [
        "dandelion woosh", "bird squawk", "trash thud", "hose spray", "ant crunch"
    ],
    "voices": ["Neighbour praise", "Neighbour tut"]
}

# 7. Visual Requirements
visuals = {
    "style": "Cartoon",
    "main_area": "Lawn",
    "elements": ["Sidewalk", "Meter", "Threat animations"]
}

# 8. UI Elements
ui = {
    "start_button": True,
    "pause_menu": True,
    "compliment_meter": True,
    "mic_feedback": "Glow indicator",
    "end_screen": "Neighbour Review"
}

# 9. Progression and Bonus
progression = {
    "difficulty_ramp": "Speed and variety",
    "bonus_levels": "Zen garden mode for perfect lawns"
}

# Zen Relaxation Levels
zen_levels = [
    {"level": "10Z", "theme": "Tea Garden",
        "reward": "+Lawn Health Boost (next 3 lvls)"},
    {"level": "20Z", "theme": "Mini Pond", 
        "reward": "+Auto-hose for dog pee (temp)"},
    {"level": "30Z", "theme": "Bonsai Courtyard", 
        "reward": "Norman flick delay +1s (next 5)"},
    {"level": "40Z", "theme": "Sakura Garden", 
        "reward": "Reduce trash rate by 20%"},
    {"level": "50Z", "theme": "Zen Sand Raking Mastery", 
        "reward": "Unlock permanent décor pieces"}
]
