import pandas as pd
from tabulate import tabulate
from config import CONFIG

def summarize(results):
    summary = {
        "player_win_rates": ["Player Wins"],
        "dealer_win_rates": ["Dealer Wins"],
        "draw_rates": ["Draws"],
        "player_bust_rates": ["Player Busts"],
        "dealer_bust_rates": ["Dealer Busts"]
    }

    for result in results:
        summary["player_win_rates"].append((result["player_wins"] / CONFIG["games_per_sim"]) * 100)
        summary["dealer_win_rates"].append((result["dealer_wins"] / CONFIG["games_per_sim"]) * 100)
        summary["draw_rates"].append((result["draws"] / CONFIG["games_per_sim"]) * 100)
        summary["player_bust_rates"].append((result["player_bust"] / CONFIG["games_per_sim"]) * 100)
        summary["dealer_bust_rates"].append((result["dealer_bust"] / CONFIG["games_per_sim"]) * 100)
    
    return summary

def display_table(summary):
    headers = ["Fixed Hit Threshold", "12", "13", "14", "15", "16", "17", "18", "19"]
    data = [summary["player_win_rates"], summary["dealer_win_rates"], summary["draw_rates"], summary["player_bust_rates"], summary["dealer_bust_rates"]]
    print(tabulate(data, headers=headers, floatfmt=".2f"))

def export_to_csv(summary):
    df = pd.DataFrame(summary)
    df.to_csv('summary.csv', index=False)