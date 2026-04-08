import sys

from myanalysis.data.config import mc_config, data_config
from myanalysis.data.df_builder import build_and_save
from myanalysis.data.datasets import get_mc_datasets, get_data_datasets


if "--data" in sys.argv:
    data_files = get_data_datasets()
    build_and_save(data_files, data_config)

else:
    mc_files = get_mc_datasets()
    build_and_save(mc_files, mc_config)