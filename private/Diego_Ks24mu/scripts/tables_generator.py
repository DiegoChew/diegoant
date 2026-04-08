from tabulate import tabulate, SEPARATING_LINE
import json
from pathlib import Path

ruta = Path(__file__).parent / "Output" / "results" / "efficiencies.json"

with open(ruta, "r") as f:
    datos = json.load(f)

# print(datos)

def pm(val, err):
    return f"{val:.6f} $\\pm$ {err:.6f}"

columnas_N = ["Stage","w40\_42","w37\_39","w35\_37","w31\_34"]
datos_N = [
    [
        "Generated", 
        datos["40_42"]["Generated"], 
        datos["37_39"]["Generated"],
        datos["35_37"]["Generated"],
        datos["31_34"]["Generated"]
        ],
    [
        "Reco", 
        datos["40_42"]["Reco"], 
        datos["37_39"]["Reco"],
        datos["35_37"]["Reco"],
        datos["31_34"]["Reco"]
        ],
    [
        "HLT2", 
        datos["40_42"]["HLT2"], 
        datos["37_39"]["HLT2"],
        datos["35_37"]["HLT2"],
        datos["31_34"]["HLT2"]
        ],
    [
        "HLT1", 
        datos["40_42"]["HLT1"], 
        datos["37_39"]["HLT1"],
        datos["35_37"]["HLT1"],
        datos["31_34"]["HLT1"]
        ],
    [
        "SelectedMuon", 
        datos["40_42"]["Selected_muon"], 
        datos["37_39"]["Selected_muon"],
        datos["35_37"]["Selected_muon"],
        datos["31_34"]["Selected_muon"]
        ],
    [
        "SelectedPID-3", 
        datos["40_42"]["Selected_PID_3"], 
        datos["37_39"]["Selected_PID_3"],
        datos["35_37"]["Selected_PID_3"],
        datos["31_34"]["Selected_PID_3"]
        ],
    [
        "ProbNNPID-3", 
        datos["40_42"]["ProbNN_PID_3"], 
        datos["37_39"]["ProbNN_PID_3"],
        datos["35_37"]["ProbNN_PID_3"],
        datos["31_34"]["ProbNN_PID_3"]
        ],
    [
        "\hline"
        ],
    [
        "SelectedPID0", 
        datos["40_42"]["Selected_PID_0"], 
        datos["37_39"]["Selected_PID_0"],
        datos["35_37"]["Selected_PID_0"],
        datos["31_34"]["Selected_PID_0"]
        ],
    [
        "ProbNNPID0", 
        datos["40_42"]["ProbNN_PID_0"], 
        datos["37_39"]["ProbNN_PID_0"],
        datos["35_37"]["ProbNN_PID_0"],
        datos["31_34"]["ProbNN_PID_0"]
        ],
]

columnas_eff = ["Efficiency","w40\_42","w37\_39","w35\_37","w31\_34", "All"]
datos_eff = [
    [
        "Reco", 
        pm(datos["40_42"]["reco_eff"],datos["40_42"]["reco_err"]), 
        pm(datos["37_39"]["reco_eff"],datos["37_39"]["reco_err"]),
        pm(datos["35_37"]["reco_eff"],datos["35_37"]["reco_err"]),
        pm(datos["31_34"]["reco_eff"],datos["31_34"]["reco_err"]),
        pm(datos["total"]["total_reco"],datos["total"]["total_reco_err"])
        ],
    [
        "HLT2", 
        pm(datos["40_42"]["hlt2_eff"],datos["40_42"]["hlt2_err"]), 
        pm(datos["37_39"]["hlt2_eff"],datos["37_39"]["hlt2_err"]),
        pm(datos["35_37"]["hlt2_eff"],datos["35_37"]["hlt2_err"]),
        pm(datos["31_34"]["hlt2_eff"],datos["31_34"]["hlt2_err"]),
        pm(datos["total"]["total_hlt2"],datos["total"]["total_hlt2_err"])
        ],
    [
        "HLT1", 
        pm(datos["40_42"]["hlt1_eff"],datos["40_42"]["hlt1_err"]), 
        pm(datos["37_39"]["hlt1_eff"],datos["37_39"]["hlt1_err"]),
        pm(datos["35_37"]["hlt1_eff"],datos["35_37"]["hlt1_err"]),
        pm(datos["31_34"]["hlt1_eff"],datos["31_34"]["hlt1_err"]),
        pm(datos["total"]["total_hlt1"],datos["total"]["total_hlt1_err"])
        ],
    [
        "SelectedMuon", 
        pm(datos["40_42"]["select_muon_eff"],datos["40_42"]["select_muon_err"]), 
        pm(datos["37_39"]["select_muon_eff"],datos["37_39"]["select_muon_err"]),
        pm(datos["35_37"]["select_muon_eff"],datos["35_37"]["select_muon_err"]),
        pm(datos["31_34"]["select_muon_eff"],datos["31_34"]["select_muon_err"]),
        pm(datos["total"]["total_select_muon"],datos["total"]["total_select_muon_err"])
        ],
    [
        "SelectedPID-3", 
        pm(datos["40_42"]["select_PID_3_eff"],datos["40_42"]["select_PID_3_err"]), 
        pm(datos["37_39"]["select_PID_3_eff"],datos["37_39"]["select_PID_3_err"]),
        pm(datos["35_37"]["select_PID_3_eff"],datos["35_37"]["select_PID_3_err"]),
        pm(datos["31_34"]["select_PID_3_eff"],datos["31_34"]["select_PID_3_err"]),
        pm(datos["total"]["total_select_PID_3"],datos["total"]["total_select_PID_3_err"])
        ],
    [
        "ProbNNPID-3", 
        pm(datos["40_42"]["probNN_PID_3_eff"],datos["40_42"]["probNN_PID_3_err"]), 
        pm(datos["37_39"]["probNN_PID_3_eff"],datos["37_39"]["probNN_PID_3_err"]),
        pm(datos["35_37"]["probNN_PID_3_eff"],datos["35_37"]["probNN_PID_3_err"]),
        pm(datos["31_34"]["probNN_PID_3_eff"],datos["31_34"]["probNN_PID_3_err"]),
        pm(datos["total"]["total_probNN_PID_3"],datos["total"]["total_probNN_PID_3_err"])
        ],
    [
        "TotalPID-3", 
        pm(datos["40_42"]["total_eff_PID_3"],datos["40_42"]["total_err_PID_3"]), 
        pm(datos["37_39"]["total_eff_PID_3"],datos["37_39"]["total_err_PID_3"]),
        pm(datos["35_37"]["total_eff_PID_3"],datos["35_37"]["total_err_PID_3"]),
        pm(datos["31_34"]["total_eff_PID_3"],datos["31_34"]["total_err_PID_3"]),
        pm(datos["total"]["total_PID_3"],datos["total"]["total_PID_3_err"])
        ],
    [
        "\hline"
        ],
    [
        "SelectedPID0", 
        pm(datos["40_42"]["select_PID_0_eff"],datos["40_42"]["select_PID_0_err"]), 
        pm(datos["37_39"]["select_PID_0_eff"],datos["37_39"]["select_PID_0_err"]),
        pm(datos["35_37"]["select_PID_0_eff"],datos["35_37"]["select_PID_0_err"]),
        pm(datos["31_34"]["select_PID_0_eff"],datos["31_34"]["select_PID_0_err"]),
        pm(datos["total"]["total_select_PID_0"],datos["total"]["total_select_PID_0_err"])
        ],
    [
        "ProbNNPID0", 
        pm(datos["40_42"]["probNN_PID_0_eff"],datos["40_42"]["probNN_PID_0_err"]), 
        pm(datos["37_39"]["probNN_PID_0_eff"],datos["37_39"]["probNN_PID_0_err"]),
        pm(datos["35_37"]["probNN_PID_0_eff"],datos["35_37"]["probNN_PID_0_err"]),
        pm(datos["31_34"]["probNN_PID_0_eff"],datos["31_34"]["probNN_PID_0_err"]),
        pm(datos["total"]["total_probNN_PID_0"],datos["total"]["total_probNN_PID_0_err"])
        ],

    [
        "TotalPID0", 
        pm(datos["40_42"]["total_eff_PID_0"],datos["40_42"]["total_err_PID_0"]), 
        pm(datos["37_39"]["total_eff_PID_0"],datos["37_39"]["total_err_PID_0"]),
        pm(datos["35_37"]["total_eff_PID_0"],datos["35_37"]["total_err_PID_0"]),
        pm(datos["31_34"]["total_eff_PID_0"],datos["31_34"]["total_err_PID_0"]),
        pm(datos["total"]["total_PID_0"],datos["total"]["total_PID_0_err"])
        ],
]

# Generar tabla en formato LaTeX
tabla_latex_1 = tabulate(datos_N, headers=columnas_N, tablefmt="latex_raw")
tabla_latex_2 = tabulate(datos_eff, headers=columnas_eff, tablefmt="latex_raw")
print(tabla_latex_1)
print(tabla_latex_2)