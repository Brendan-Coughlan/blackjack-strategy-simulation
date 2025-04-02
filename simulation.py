from tqdm import tqdm
from deck import *
from config import CONFIG
from strategies import use_strategy

def run_game():
    results = {"player_wins": 0, "dealer_wins": 0, "draws": 0, "player_bust": 0, "dealer_bust": 0}
    deck = populate_deck(CONFIG["num_decks"])
    shuffle_deck(deck)
    
    dealer_hand = deal_hand(deck, 2)
    player_hand = deal_hand(deck, 2)
    dealer_hand_value = calculate_hand_value(dealer_hand)
    player_hand_value = calculate_hand_value(player_hand)
    
    while use_strategy(player_hand_value):
        player_hand.extend(deal_hand(deck))
        player_hand_value = calculate_hand_value(player_hand)

    while dealer_hand_value < CONFIG["dealer_stand_threshold"]:
        dealer_hand.extend(deal_hand(deck))
        dealer_hand_value = calculate_hand_value(dealer_hand)
        
    if player_hand_value > 21:
        results["dealer_wins"] += 1
        results["player_bust"] += 1
    elif dealer_hand_value > 21:
        results["player_wins"] += 1
        results["dealer_bust"] += 1
    elif dealer_hand_value > player_hand_value:
        results["dealer_wins"] += 1
    elif dealer_hand_value < player_hand_value:
        results["player_wins"] += 1
    else:
        results["draws"] += 1
        
    return results

def run_simulation():
    simulation_results = {"player_wins": 0, "dealer_wins": 0, "draws": 0, "player_bust": 0, "dealer_bust": 0}
    for i in tqdm(range(CONFIG["games_per_sim"]), desc="Loading...", leave=False):
        game_results = run_game()
        for key in simulation_results:
            if key in game_results:
                simulation_results[key] += game_results[key]
    return simulation_results