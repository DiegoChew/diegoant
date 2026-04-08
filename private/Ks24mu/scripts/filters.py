import sys

from myanalysis.filters.muon import mc_filter_muon, data_filter_muon
from myanalysis.filters.PID import mc_filter_PID, data_filter_PID

if "--PID_data" in sys.argv:
    data_filter_PID(0)

elif "--PID_mc" in sys.argv:
    mc_filter_PID(0)

elif "--muon_data" in sys.argv:
    data_filter_muon()

elif "--muon_mc" in sys.argv:
    mc_filter_muon()

else:
    print("ERROR")
