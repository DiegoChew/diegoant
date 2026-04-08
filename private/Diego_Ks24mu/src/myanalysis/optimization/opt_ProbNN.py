import matplotlib.pyplot as plt
from myanalysis.data.selections import probNN_filter_v2
import pandas as pd
import numpy as np


def efficiency(df_before, df_after):
    if len(df_before) == 0:
        return 0
    return len(df_after) / len(df_before)

def ProbNN_opt():
    
    df_mc = pd.read_parquet("Output/dataframes/MC_PID_all.parquet")
    df_data = pd.read_parquet("Output/dataframes/DATA_PID_all.parquet")

    cuts = np.linspace(0, 1, 50)  


    scores = []
    eff_mc_list = []
    eff_data_list = []

    N_mc_before = len(df_mc)
    N_data_before = len(df_data)

    for c in cuts:

        # aplica corte PID
        df_mc_cut = probNN_filter_v2(df_mc, c)
        df_data_cut = probNN_filter_v2(df_data, c)

        # eficiencias
        eff_mc = efficiency(df_mc, df_mc_cut)
        eff_data = efficiency(df_data, df_data_cut)

        # score
        if eff_data > 0:
            score = eff_mc / np.sqrt(eff_data)
        else:
            score = 0

        eff_mc_list.append(eff_mc)
        eff_data_list.append(eff_data)
        scores.append(score)

    best_index = np.argmax(scores)
    best_cut = cuts[best_index]
    best_score = scores[best_index]

    print("Best cut:", best_cut)
    print("Best score:", best_score)

    plt.figure(figsize=(8,6))

    plt.axvline(best_cut, linestyle="--", label=f"Best cut = {best_cut:.2f}")
    plt.plot(cuts, scores, label=r"$\epsilon_{MC}/\sqrt{\epsilon_{DATA}}$")
    plt.plot(cuts, eff_mc_list, "--", label=r"$\epsilon_{MC}$")
    plt.plot(cuts, eff_data_list, "--", label=r"$\epsilon_{DATA}$")

    plt.xlabel("ProbNN cut")
    plt.ylabel("Value")
    plt.title("ProbNN optimization between [0, 1]")

    plt.grid(alpha=0.3)
    plt.legend()

    plt.tight_layout()
    plt.savefig("Output/plots/data/ProbNN_optimization_01.png", dpi=300)
    plt.show()
    plt.close()