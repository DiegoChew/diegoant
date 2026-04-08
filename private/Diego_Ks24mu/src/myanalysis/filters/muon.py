import pandas as pd
import os
from myanalysis.data.datasets import get_data_datasets, get_mc_datasets
from myanalysis.data.selections import muon_filter, dimuon_filter, truth_matching


def mc_filter_muon():
    mc_files = get_mc_datasets()
    versions = list(mc_files.keys())

    mc_muon_total = []  

    for v in versions:

        def load(key):
            return pd.read_parquet(f"Output/dataframes/{v}_{key}.parquet")

        df_Loose = load("Loose")

        df_HLT2 = truth_matching(df_Loose)
        df_HLT1 = dimuon_filter(df_HLT2)
        df_Muon = muon_filter(df_HLT1)

        mc_muon_total.append(df_Muon)  

    df_mc_muon_all = pd.concat(mc_muon_total, ignore_index=True)

    os.makedirs("Output/dataframes", exist_ok=True)

    df_mc_muon_all.to_parquet("Output/dataframes/MC_muon_all.parquet")

    print("Saved:", len(df_mc_muon_all), "events")

def data_filter_muon():
    data_files = get_data_datasets()
    data_versions = list(data_files.keys())

    data_muon_total = []  

    for v in data_versions:

        df_data = pd.read_parquet(f"Output/dataframes/{v}_DATA.parquet")

        df_HLT1 = dimuon_filter(df_data)
        df_Muon = muon_filter(df_HLT1)

        data_muon_total.append(df_Muon)  

    df_data_muon_all = pd.concat(data_muon_total, ignore_index=True)

    os.makedirs("Output/dataframes", exist_ok=True)

    df_data_muon_all.to_parquet("Output/dataframes/DATA_muon_all.parquet")

    print("Saved:", len(df_data_muon_all), "events")