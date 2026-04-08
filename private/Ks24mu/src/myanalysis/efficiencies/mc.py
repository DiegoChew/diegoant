import matplotlib.pyplot as plt
# import config
import pandas as pd
import numpy as np
from myanalysis.data.datasets import get_mc_datasets
from myanalysis.data.selections import muon_filter, PID_filter, dimuon_filter, truth_matching, probNN_filter, angle_filter

# from myanalysis.utils.efficiencies import compute_efficiencies
# from utils.histograms import ks_mass_flow
import json
# import os

# def convert(o):
#     if isinstance(o, np.generic):
#         return o.item()
#     return o

# os.makedirs("Output/results", exist_ok=True)



# def build_mc_filtered(version):

#     def load(key):
#         return pd.read_parquet(f"Output/dataframes/{version}_{key}.parquet")

#     df_MC = load("MC")
#     df_Reco = load("Reco")
#     df_Loose = load("Loose")

  
#     df_HLT2 = truth_matching(df_Loose)
#     df_HLT1 = dimuon_filter(df_HLT2)
#     df_Muon = muon_filter(df_HLT1)

#     df_PID_3 = PID_filter(df_Muon, -3, -3, -3, -3)
#     df_PID_0 = PID_filter(df_Muon, 1.56, 1.56, 1.56, 1.56)

#     df_ProbNN_3 = probNN_filter(df_PID_3)
#     df_ProbNN_0 = probNN_filter(df_PID_0)

#     return {
#         "MC": df_MC,
#         "Reco": df_Reco,
#         "HLT2": df_HLT2,
#         "HLT1": df_HLT1,
#         "Selected_muon": df_Muon,
#         "Selected_PID_3": df_PID_3,
#         "Selected_PID_0": df_PID_0,
#         "ProbNN_PID_3": df_ProbNN_3,
#         "ProbNN_PID_0": df_ProbNN_0,
#     }




def run_mc_efficiencies(P=0, angle = 0.0015):

    per_version = {}

    total_MC = total_Reco = total_HLT2 = total_HLT1 = total_Muon = total_PID = total_Angle = 0

    mc_files = get_mc_datasets()
    versions = list(mc_files.keys())

    for v in versions:

        df_MC = pd.read_parquet(f"Output/dataframes/{v}_MC.parquet")
        df_Reco = pd.read_parquet(f"Output/dataframes/{v}_Reco.parquet")
        df_Loose = pd.read_parquet(f"Output/dataframes/{v}_Loose.parquet")

        df_Hlt2  = truth_matching(df_Loose)
        df_Hlt1  = dimuon_filter(df_Hlt2)
        df_Muon  = muon_filter(df_Hlt1)
        df_PID   = PID_filter(df_Muon, P, P, P, P)
        df_angle = angle_filter(df_PID, angle)

         
        MC    = len(df_MC)
        Reco  = len(df_Reco)
        Hlt2  = len(df_Hlt2)
        Hlt1  = len(df_Hlt1)
        Muon  = len(df_Muon)
        PID   = len(df_PID)
        Angle = len(df_angle)

        reco_eff  = Reco  / MC   if MC else 0
        Hlt2_eff  = Hlt2  / Reco if Reco else 0
        Hlt1_eff  = Hlt1  / Hlt2 if Hlt2 else 0
        Muon_eff  = Muon  / Hlt1 if Hlt1 else 0
        PID_eff   = PID   / Muon if Muon else 0
        Angle_eff = Angle / PID  if PID else 0

        reco_err  = np.sqrt(reco_eff * (1 - reco_eff) / MC) if MC else 0
        Hlt2_err  = np.sqrt(Hlt2_eff * (1 - Hlt2_eff) / Reco) if Reco else 0
        Hlt1_err  = np.sqrt(Hlt1_eff * (1 - Hlt1_eff) / Hlt2) if Hlt2 else 0
        Muon_err  = np.sqrt(Muon_eff * (1 - Muon_eff) / Hlt1) if Hlt1 else 0
        PID_err   = np.sqrt(PID_eff * (1 - PID_eff) / Muon) if Muon else 0
        Angle_err = np.sqrt(Angle_eff * (1 - Angle_eff) / PID) if PID else 0

        total_v_eff = reco_eff * Hlt2_eff * Hlt1_eff * Muon_eff * PID_eff * Angle_eff
        total_v_err = total_v_eff * np.sqrt(
            (reco_err/reco_eff)**2 +
            (Hlt2_err/Hlt2_eff)**2 +
            (Hlt1_err/Hlt1_eff)**2 +
            (Muon_err/Muon_eff)**2 +
            (PID_err/PID_eff)**2 +
            (Angle_err/Angle_eff)**2 
        ) 

        per_version[v] = {
            "MC": [MC,0,0],
            "Reco": [Reco, reco_eff, reco_err],
            "Hlt2": [Hlt2, Hlt2_eff, Hlt2_err],
            "Hlt1": [Hlt1, Hlt1_eff, Hlt1_err],
            "Muon": [Muon, Muon_eff, Muon_err],
            "PID": [PID, PID_eff, PID_err],
            "Angle": [Angle, Angle_eff, Angle_err],
            "total_v": [0, total_v_eff, total_v_err]
        }

        total_MC    += MC
        total_Reco  += Reco
        total_HLT2  += Hlt2
        total_HLT1  += Hlt1
        total_Muon  += Muon
        total_PID   += PID
        total_Angle += Angle

    total_Reco_eff  = total_Reco  / total_MC   if total_MC else 0
    total_Hlt2_eff  = total_HLT2  / total_Reco if total_Reco else 0
    total_Hlt1_eff  = total_HLT1  / total_HLT2 if total_HLT2 else 0
    total_Muon_eff  = total_Muon  / total_HLT1 if total_HLT1 else 0
    total_PID_eff   = total_PID   / total_Muon if total_Muon else 0
    total_Angle_eff = total_Angle / total_PID  if total_PID else 0

    total_Reco_err  = np.sqrt(total_Reco_eff * (1 - total_Reco_eff) / total_MC)    if total_MC else 0
    total_Hlt2_err  = np.sqrt(total_Hlt2_eff * (1 - total_Hlt2_eff) / total_Reco)  if total_Reco else 0
    total_Hlt1_err  = np.sqrt(total_Hlt1_eff * (1 - total_Hlt1_eff) / total_HLT2)  if total_HLT2 else 0
    total_Muon_err  = np.sqrt(total_Muon_eff * (1 - total_Muon_eff) / total_HLT1)  if total_HLT1 else 0
    total_PID_err   = np.sqrt(total_PID_eff * (1 - total_PID_eff) / total_Muon)    if total_Muon else 0
    total_Angle_err = np.sqrt(total_Angle_eff * (1 - total_Angle_eff) / total_PID) if total_PID else 0


    total_eff = total_Reco_eff * total_Hlt2_eff * total_Hlt1_eff * total_Muon_eff * total_PID_eff * total_Angle_eff
    total_err =  total_eff * np.sqrt(
            (total_Reco_err/total_Reco_eff)**2 +
            (total_Hlt2_err/total_Hlt2_eff)**2 +
            (total_Hlt1_err/total_Hlt1_eff)**2 +
            (total_Muon_err/total_Muon_eff)**2 +
            (total_PID_err/total_PID_eff)**2 +
            (total_Angle_err/total_Angle_eff)**2 
        )

    results = {
        "totals": {
            "MC": [total_MC,0,0],
            "Reco": [total_Reco, total_Reco_eff, total_Reco_err],
            "Hlt2": [total_HLT2, total_Hlt2_eff, total_Hlt2_err],
            "Hlt1": [total_HLT1, total_Hlt1_eff, total_Hlt1_err],
            "Muon": [total_Muon, total_Muon_eff, total_Muon_err],
            "PID": [total_PID, total_PID_eff, total_PID_err],
            "Angle": [total_Angle, total_Angle_eff, total_Angle_err],
            "total": [0, total_eff, total_err]
        },
        "per_version": per_version
    }

    with open("Output/results/mc_summary.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Saved: Output/results/mc_summary.json")

if __name__ == "__main__":
    run_mc_efficiencies()
##########################################

# bins = np.linspace(400, 600, 100)  
# hist_total = np.zeros(len(bins) - 1)

# for v in data_versions:
#     path = f"Output/dataframes/{v}_DATA.parquet"
#     print(f"Loading: {path}")

#     df = pd.read_parquet(path)

#     hist, _ = np.histogram(df["KS_M"], bins=bins)
#     hist_total += hist

# total_events = hist_total.sum()

# # plot final
# plt.step(bins[:-1], hist_total, where="mid")

# plt.xlabel("Ks_M")
# plt.ylabel("Events")
# plt.title(f"DATA - Combined (Total: {int(total_events)})")

# plt.savefig("Output/plots/DATA_KsM_all.png")
# plt.close()


