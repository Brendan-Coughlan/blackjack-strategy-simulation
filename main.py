from simulation import *
from results import *
from config import CONFIG

full_results = []
player_stand_thresholds = list(range(12, 20))

for player_stand_threshold in tqdm(player_stand_thresholds, desc="Loading...", leave=False):
    CONFIG["player_stand_threshold"] = player_stand_threshold
    simulation_results = run_simulation()
    full_results.append(simulation_results)

summary = summarize(full_results)
display_table(summary)
export_to_csv(summary)