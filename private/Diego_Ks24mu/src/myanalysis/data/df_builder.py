import pandas as pd
import uproot
import numpy as np

def calculate_angle(L1_PX, L1_PY, L1_PZ, L1_P, L2_PX, L2_PY, L2_PZ, L2_P):
    p_X = L1_PX * L2_PX
    p_Y = L1_PY * L2_PY
    p_Z = L1_PZ * L2_PZ
    cos_theta = (p_X + p_Y + p_Z) / (L1_P * L2_P)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    theta = np.arccos(cos_theta)
    return theta 

def process_file_to_df(file_path, tree_path, vars_to_use, apply_sideband=False, add_angles=False):
    try:
        with uproot.open(file_path + ":" + tree_path) as events:

            # -------------------------
            # FILTRAR VARIABLES EXISTENTES
            # -------------------------
            available = events.keys()
            vars_existing = [v for v in vars_to_use if v in available]

            missing = set(vars_to_use) - set(vars_existing)
            if missing:
                print(f"Missing in {tree_path}: {missing}")

            df = events.arrays(vars_existing, library="pd")

            # -------------------------
            # SIDE BAND 
            # -------------------------
            if apply_sideband and "KS_M" in df.columns:
                df = df[
                    (df["KS_M"] > 400) &
                    (df["KS_M"] < 600) &
                    ((df["KS_M"] < 490) | (df["KS_M"] > 510))
                ]

            # -------------------------
            # ÁNGULOS 
            # -------------------------
            if add_angles:

                required_cols = [
                    "L1_PX","L1_PY","L1_PZ","L1_P",
                    "L2_PX","L2_PY","L2_PZ","L2_P",
                    "L3_PX","L3_PY","L3_PZ","L3_P",
                    "L4_PX","L4_PY","L4_PZ","L4_P"
                ]

                if all(col in df.columns for col in required_cols):

                    angles = {}

                    angles["theta_12"] = calculate_angle(
                        df["L1_PX"], df["L1_PY"], df["L1_PZ"], df["L1_P"],
                        df["L2_PX"], df["L2_PY"], df["L2_PZ"], df["L2_P"]
                    )

                    angles["theta_13"] = calculate_angle(
                        df["L1_PX"], df["L1_PY"], df["L1_PZ"], df["L1_P"],
                        df["L3_PX"], df["L3_PY"], df["L3_PZ"], df["L3_P"]
                    )

                    angles["theta_14"] = calculate_angle(
                        df["L1_PX"], df["L1_PY"], df["L1_PZ"], df["L1_P"],
                        df["L4_PX"], df["L4_PY"], df["L4_PZ"], df["L4_P"]
                    )

                    angles["theta_23"] = calculate_angle(
                        df["L2_PX"], df["L2_PY"], df["L2_PZ"], df["L2_P"],
                        df["L3_PX"], df["L3_PY"], df["L3_PZ"], df["L3_P"]
                    )

                    angles["theta_24"] = calculate_angle(
                        df["L2_PX"], df["L2_PY"], df["L2_PZ"], df["L2_P"],
                        df["L4_PX"], df["L4_PY"], df["L4_PZ"], df["L4_P"]
                    )

                    angles["theta_34"] = calculate_angle(
                        df["L3_PX"], df["L3_PY"], df["L3_PZ"], df["L3_P"],
                        df["L4_PX"], df["L4_PY"], df["L4_PZ"], df["L4_P"]
                    )

                    df_angles = pd.DataFrame(angles)

                    df = pd.concat([df, df_angles], axis=1)

                else:
                    print(f"Skipping angles in {tree_path} (missing columns)")

            return df

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return pd.DataFrame()


def build_and_save(files, config):

    import os
    out_dir = "Output/dataframes"
    os.makedirs(out_dir, exist_ok=True)

    for version, filelist in files.items():

        print(f"\n Version: {version}")

        for key, cfg in config.items():

            all_dfs = []

            for file in filelist:

                df = process_file_to_df(
                    file,
                    cfg["tree"],
                    cfg["vars"],
                    apply_sideband=cfg["sideband"],
                    add_angles=cfg["add_angles"]
                )

                print(f"{version} | {key} | {len(df)} events")

                all_dfs.append(df)

            df_concat = pd.concat(all_dfs, ignore_index=True)

            path = f"{out_dir}/{version}_{key}.parquet"
            df_concat.to_parquet(path)

            print(f" Saved: {path}")