import random
from config import CONFIG

def fixed_threshold_strategy(hand_value):
    return hand_value < CONFIG["player_stand_threshold"]

def random_threshold_strategy(hand_value):
    threshold = random.randint(12, 19)
    return hand_value < threshold

def use_strategy(hand_value):
    if CONFIG["player_strategy"] == "fixed_threshold":
        return fixed_threshold_strategy(hand_value)
    elif CONFIG["player_strategy"] == "random_threshold":
        return random_threshold_strategy(hand_value)
    else:
        raise ValueError("Strategy not recognized")
