
from myanalysis.data.datasets import get_data_datasets
from myanalysis.data.selections import muon_filter, PID_filter, dimuon_filter, probNN_filter_v2, angle_filter

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import json

def plot_histogram(bins, hist, total, title, filename, label):

    plt.figure(figsize=(8, 6))
    plt.step(bins[:-1], hist, where="mid", linewidth=1.5, label=label)

    plt.xlabel(r"$K_S$ Mass [MeV/$c^2$]", fontsize=13)
    plt.ylabel("Events", fontsize=13)
    plt.title(f"{title} (Total: {int(total)})", fontsize=14)

    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()

    plt.savefig(filename, dpi=300)
    plt.close()


def run_data_analysis(p=0,ang=0.0015):

    plt.style.use("seaborn-v0_8-muted")
    os.makedirs("Output/plots/data", exist_ok=True)
    os.makedirs("Output/results", exist_ok=True)

    data_files = get_data_datasets()
    data_versions = list(data_files.keys())

    bins = np.linspace(400, 600, 100)

    total_HLT2 = total_HLT1 = total_muon = total_PID = total_Angle = 0

    
    per_version = {}

    hist_hlt2_total = np.zeros(len(bins) - 1)
    hist_hlt1_total = np.zeros(len(bins) - 1)
    hist_muon_total = np.zeros(len(bins) - 1)
    hist_PID_total = np.zeros(len(bins) - 1)
    hist_Angle_total = np.zeros(len(bins) - 1)

    for v in data_versions:

        df_data = pd.read_parquet(f"Output/dataframes/{v}_DATA.parquet")

        n_HLT2 = len(df_data)
        hist_hlt2_total += np.histogram(df_data["KS_M"], bins=bins)[0]

        df_hlt1 = dimuon_filter(df_data)
        n_HLT1 = len(df_hlt1)
        hist_hlt1_total += np.histogram(df_hlt1["KS_M"], bins=bins)[0]

        df_muon = muon_filter(df_hlt1)
        n_muon = len(df_muon)
        hist_muon_total += np.histogram(df_muon["KS_M"], bins=bins)[0]

        df_PID = PID_filter(df_muon, p, p, p, p)
        n_PID = len(df_PID)
        hist_PID_total += np.histogram(df_PID["KS_M"], bins=bins)[0]

        df_Angle = angle_filter(df_PID, ang)
        n_Angle = len(df_Angle)
        hist_Angle_total += np.histogram(df_Angle["KS_M"], bins=bins)[0]

        # guardar por versión
        per_version[v] = {
            "HLT2": n_HLT2,
            "HLT1": n_HLT1,
            "Muon": n_muon,
            "PID": n_PID,
            "Angle": n_Angle,
        }

        total_HLT2 += n_HLT2
        total_HLT1 += n_HLT1
        total_muon += n_muon
        total_PID += n_PID
        total_Angle += n_Angle

    # plots 
    plot_histogram(bins, hist_hlt2_total, total_HLT2, "HLT2_DATA_KsM_all", "Output/plots/data/HLT2_DATA_KsM_all.png", "HLT2")
    plot_histogram(bins, hist_hlt1_total, total_HLT1, "HLT1_DATA_KsM_all", "Output/plots/data/HLT1_DATA_KsM_all.png", "HLT1")
    plot_histogram(bins, hist_muon_total, total_muon, "Muon_DATA_KsM_all", "Output/plots/data/Muon_DATA_KsM_all.png", "Muon")
    plot_histogram(bins, hist_PID_total, total_PID, "PID_DATA_KsM_all", "Output/plots/data/PID_DATA_KsM_all.png", "PID")
    plot_histogram(bins, hist_Angle_total, total_Angle, "Angle_DATA_KsM_all", "Output/plots/data/Angle_DATA_KsM_all.png", "Angle")

    # # eficiencias
    # eff = {
    #     "HLT1": total_HLT1 / total_HLT2 if total_HLT2 else 0,
    #     "Muon": total_muon / total_HLT1 if total_HLT1 else 0,
    #     "PID": total_PID / total_muon if total_muon else 0,
    #     "Angle": total_Angle / total_PID if total_PID else 0,
    # }

    # JSON final
    results = {
        "totals": {
            "HLT2": total_HLT2,
            "HLT1": total_HLT1,
            "Muon": total_muon,
            "PID": total_PID,
            "Angle": total_Angle,
        },
        # "efficiencies": eff,
        "per_version": per_version
    }

    with open("Output/results/data_summary.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Saved: Output/results/data_summary.json")

    return results


if __name__ == "__main__":
    run_data_analysis()