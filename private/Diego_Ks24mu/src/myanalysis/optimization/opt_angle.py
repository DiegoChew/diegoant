import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from myanalysis.data.selections import angle_filter


# =========================
# UTILIDAD
# =========================
def efficiency(df_before, df_after):
    if len(df_before) == 0:
        return 0
    return len(df_after) / len(df_before)

def angle_opt():
    # =========================
    # CARGA DE DATOS
    # =========================
    df_data = pd.read_parquet("Output/dataframes/DATA_PID0_all.parquet")
    df_mc = pd.read_parquet("Output/dataframes/MC_PID0_all.parquet")


    # =========================
    # SCAN FINO ENTRE 0.001 y 0.002
    # =========================
    fine_cuts = np.linspace(0.001, 0.002, 21)

    print("\n=== FINE SCAN CUTS ===")
    results = []

    for cut_val in fine_cuts:

        df_mc_cut = angle_filter(df_mc, cut_val)
        df_data_cut = angle_filter(df_data, cut_val)

        eff_mc = efficiency(df_mc, df_mc_cut)
        eff_data = efficiency(df_data, df_data_cut)

        n_mc = len(df_mc_cut)
        n_data = len(df_data_cut)

        results.append({
            "cut": cut_val,
            "eff_mc": eff_mc,
            "eff_data": eff_data,
            "n_mc": n_mc,
            "n_data": n_data
        })

        print(f"Angle cut = {cut_val:.6f} | eff MC = {eff_mc:.4f}, MC events = {n_mc} | eff DATA = {eff_data:.4f}, DATA events = {n_data}, initial data = {len(df_data)}")


    # =========================
    # PLOT: HISTOGRAMAS PARA LOS 5 CORTES
    # =========================
    xmin, xmax = 400, 600
    bins = 100

    plt.figure(figsize=(8,6))

    # histograma sin corte
    counts_before, edges = np.histogram(df_data["KS_M"], bins=bins, range=(xmin, xmax))
    centers = 0.5 * (edges[1:] + edges[:-1])
    plt.step(centers, counts_before, where="mid", label="No cut", alpha=0.5)

    # histogramas para cada corte fino
    for r in results:
        df_cut = angle_filter(df_data, r["cut"])
        counts, _ = np.histogram(df_cut["KS_M"], bins=bins, range=(xmin, xmax))
        plt.step(centers, counts, where="mid", label=f"cut={r['cut']:.6f}, eff MC={r['eff_mc']:.3f}")

    # región ciega
    plt.axvspan(490, 510, color="gray", alpha=0.2, label="Blind region")

    plt.xlabel("KS_M")
    plt.ylabel("Counts")
    plt.title("Mass distributions for angle cut 0.0014")
    plt.legend(fontsize=8)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("Output/plots/data/mass_angle14_cuts.png", dpi=300)
    plt.show()
    plt.close()



