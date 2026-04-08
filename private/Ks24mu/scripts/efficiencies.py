import sys

from myanalysis.efficiencies.mc import run_mc_efficiencies
from myanalysis.efficiencies.data import run_data_analysis

if "--data" in sys.argv:
    run_data_analysis(p=0,ang=0.0015)

else:
    run_mc_efficiencies(P=0, angle = 0.0015)