.PHONY: mc data all clean

load_mc:
	python scripts/data_loader.py

load_data:
	python scripts/data_loader.py --data

load_all:
	make load_mc
	make load_data

clean_data:
	rm -rf Output/dataframes/*.parquet

mc_eff:
	python scripts/efficiencies.py

data_counts:
	python scripts/efficiencies.py --data

PID_data_filter:
	python scripts/filters.py --PID_data

PID_mc_filter:
	python scripts/filters.py --PID_mc

muon_data_filter:
	python scripts/filters.py --muon_data

muon_mc_filter:
	python scripts/filters.py --muon_mc

PID_filter:
	make PID_data_filter
	make PID_mc_filter

muon_filter:
	make muon_data_filter
	make muon_mc_filter

PID_opt:
	python scripts/optimize_variables.py --PID

Angle_opt:
	python scripts/optimize_variables.py --angle

ProbNN_opt:
	python scripts/optimize_variables.py --ProbNN