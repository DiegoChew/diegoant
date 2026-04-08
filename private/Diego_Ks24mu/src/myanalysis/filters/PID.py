import pandas as pd
import os
from myanalysis.data.selections import PID_filter


def mc_filter_PID(c):
    df_mc = pd.read_parquet(f"Output/dataframes/MC_muon_all.parquet")
    df_mc_PID = PID_filter(df_mc, c, c, c, c)

    os.makedirs("Output/dataframes", exist_ok=True)

    df_mc_PID.to_parquet(f"Output/dataframes/MC_PID{c}_all.parquet")

    print("Saved:", len(df_mc_PID), "events")

##############

def data_filter_PID(c):
    df_data = pd.read_parquet(f"Output/dataframes/DATA_muon_all.parquet")
    df_data_PID = PID_filter(df_data, c, c, c, c)

    os.makedirs("Output/dataframes", exist_ok=True)

    df_data_PID.to_parquet(f"Output/dataframes/DATA_PID{c}_all.parquet")

    print("Saved:", len(df_data_PID), "events")

