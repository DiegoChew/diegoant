import matplotlib.pyplot as plt
from myanalysis.data.selections import PID_filter
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import quad

def expo(x, A, k):
    return A * np.exp(-k * x)

def efficiency(df_before, df_after):
    if len(df_before) == 0:
        return 0
    return len(df_after) / len(df_before)

def fit_exponential(df, mass_col, xmin, xmax, exclude_min, exclude_max, bins=60):

    data = df[mass_col]

    # Histograma
    counts, edges = np.histogram(data, bins=bins, range=(xmin, xmax))
    centers = 0.5 * (edges[1:] + edges[:-1])

    # Excluir región (blind)
    mask = (centers < exclude_min) | (centers > exclude_max)

    x_fit = centers[mask]
    y_fit = counts[mask]

    # Ajuste
    popt, _ = curve_fit(expo, x_fit, y_fit, p0=(max(y_fit), 0.001))

    A, k = popt

    return A, k, centers, counts
    
def integrate_exponential(A, k, xmin, xmax):
    integral, _ = quad(lambda x: expo(x, A, k), xmin, xmax)
    return integral

def PID_opt():
    
    df_mc = pd.read_parquet("Output/dataframes/MC_muon_all.parquet")
    df_data = pd.read_parquet("Output/dataframes/DATA_muon_all.parquet")

    cuts = np.linspace(-25, 10, 200)  


    scores = []
    eff_mc_list = []
    bkg_list = []

    for c in cuts:

        # aplica corte PID
        df_mc_cut = PID_filter(df_mc, c, c, c, c)
        df_data_cut = PID_filter(df_data, c, c, c, c)

        # eficiencia MC
        eff_mc = efficiency(df_mc, df_mc_cut)

        #  FIT EXPONENCIAL (sidebands)
        try:
            A, k, _, _ = fit_exponential(
                df_data_cut,
                mass_col="KS_M",   
                xmin=400,
                xmax=600,
                exclude_min=490,
                exclude_max=510
            )

            #  INTEGRAR EN REGIÓN CIEGA
            N_bkg = integrate_exponential(A, k, 400, 600)

        except:
            N_bkg = 0
            print("algo pasa")

        #  SCORE NUEVO
        if N_bkg > 0:
            score = (3*eff_mc) / (2*np.sqrt(N_bkg))
        else:
            score = 0

        eff_mc_list.append(eff_mc)
        bkg_list.append(N_bkg)
        scores.append(score)



    best_index = np.argmax(scores)
    best_cut = cuts[best_index]
    best_score = scores[best_index]

    print("Best cut:", best_cut)
    print("Best score:", best_score)

    #######################################################333
    df_data_before = df_data
    df_data_after = PID_filter(df_data, best_cut, best_cut, best_cut, best_cut)
    df_data_cero = PID_filter(df_data, 0, 0, 0, 0)

    A, k, centers, counts = fit_exponential(
        df_data_after,
        mass_col="KS_M",
        xmin=400,
        xmax=600,
        exclude_min=490,
        exclude_max=510
    )

    plt.figure(figsize=(8,6))

    plt.axvline(best_cut, linestyle="--", label=f"Best cut = {best_cut:.2f}")
    plt.plot(cuts, scores, label=r"$3\epsilon_{MC}/2\sqrt{N_{bkg}}$")
    plt.plot(cuts, eff_mc_list, "--", label=r"$\epsilon_{MC}$")
    # plt.plot(cuts, bkg_list, "--", label=r"$N_{bkg}$")

    plt.xlabel("PID cut")
    plt.ylabel("Value")
    plt.title("PID optimization between [-25, 10]")

    plt.grid(alpha=0.3)
    plt.legend()

    plt.tight_layout()
    plt.savefig("Output/plots/data/pid_optimization_2510.png", dpi=300)
    plt.show()
    plt.close()

    plt.figure(figsize=(8,6))

    ###############################################################################33333
    bins = 100


    plt.hist(
        df_data_before["KS_M"],
        bins=bins,
        range=(400, 600),
        histtype="step",
        label="Data before cut"
    )

    # Después del corte
    plt.hist(
        df_data_after["KS_M"],
        bins=bins,
        range=(400, 600),
        histtype="step",
        label="Data after cut"
    )

    # # Fit exponencial
    # x_fit = np.linspace(400, 600, 300)
    # y_fit = expo(x_fit, A, k)

    # plt.plot(x_fit, y_fit, label="Exponential fit")

    # Región ciega
    plt.axvspan(490, 510, alpha=0.2, label="Blind region")

    plt.xlabel("KS_M")
    plt.ylabel("Events")
    plt.title(f"Best cut = {best_cut:.2f}")

    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("Output/plots/data/mass_fit_best_cut.png", dpi=300)
    plt.show()
    plt.close()
    ############################################################################3

    plt.figure(figsize=(8,6))

    bins = 60

    plt.hist(
        df_data_cero["KS_M"],
        bins=bins,
        range=(400, 600),
        histtype="step",
        label=f"Data after cut = {0:.2f} counts: {len(df_data_cero)}"
    )

    plt.hist(
        df_data_after["KS_M"],
        bins=bins,
        range=(400, 600),
        histtype="step",
        label=f"Data after cut = {best_cut:.2f} counts: {len(df_data_after)}"
    )


    plt.axvspan(490, 510, alpha=0.2, label="Blind region")

    plt.xlabel("KS_M")
    plt.ylabel("Events")
    plt.title("Mass distribution after optimal cut")

    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("Output/plots/data/PID0_best_DATA_KsM_all.png", dpi=300)
    plt.show()
    plt.close()