from apd import AnalysisData


def get_mc_datasets():

    datasets = AnalysisData("rd", "kaons_run3")

    # ---------------- w40_42 ----------------
    magup = datasets(
        config="mc",
        polarity="magup",
        eventtype="34114102",
        datatype="2024",
        filetype="tuple.root",
        name="mc_ks4mu_34114102_2024-w40-42_magup_nu7p6",
        version="v1r3175"
    )

    magdown = datasets(
        config="mc",
        polarity="magdown",
        eventtype="34114102",
        datatype="2024",
        filetype="tuple.root",
        name="mc_ks4mu_34114102_2024-w40-42_magdown_nu7p6",
        version="v1r3175"
    )

    files_40_42 = magup[:] + magdown[:]

    # ---------------- w37_39 ----------------
    files_37_39 = datasets(
        config="mc",
        polarity="magdown",
        eventtype="34114102",
        datatype="2024",
        filetype="tuple.root",
        name="mc_ks4mu_34114102_2024-w37-39_magdown_nu6p3",
        version="v1r3175"
    )[:]

    # ---------------- w35_37 ----------------
    files_35_37 = datasets(
        config="mc",
        polarity="magup",
        eventtype="34114102",
        datatype="2024",
        filetype="tuple.root",
        name="mc_ks4mu_34114102_2024-w35-37_magup_nu6p3",
        version="v1r3175"
    )[:]

    # ---------------- w31_34 ----------------
    files_31_34 = datasets(
        config="mc",
        polarity="magup",
        eventtype="34114102",
        datatype="2024",
        filetype="tuple.root",
        name="mc_ks4mu_34114102_2024-w31-34_magup_nu6p3",
        version="v1r3175"
    )[:]

    return {
        "40_42": files_40_42,
        "37_39": files_37_39,
        "35_37": files_35_37,
        "31_34": files_31_34
    }
    #########################################
def get_data_datasets():

    datasets = AnalysisData("rd", "kaons_run3")

    return {
        "24_up_c2": datasets(
            config="lhcb", 
            polarity="magup", 
            eventtype="94000000", 
            datatype="2024", 
            filetype="ftuple.root", 
            name="data_24_magup_24c2a", 
            version="v1r3175"
            )[:],
        "24_up_c3": datasets(
            config="lhcb", 
            polarity="magup", 
            eventtype="94000000", 
            datatype="2024", 
            filetype="ftuple.root", 
            name = "data_24_magup_24c3a", 
            version = "v1r3175"
            )[:],
        "24_up_c4": datasets(
            config="lhcb", 
            polarity="magup", 
            eventtype="94000000", 
            datatype="2024", 
            filetype="ftuple.root", 
            name = "data_24_magup_24c4a", 
            version = "v1r3175"
            )[:],

        "24_down_c3": datasets(
            config="lhcb", 
            polarity="magdown", 
            eventtype="94000000", 
            datatype="2024", 
            filetype="ftuple.root", 
            name = "data_24_magdown_24c3a", 
            version = "v1r3175"
            )[:],
        "24_down_c4": datasets(
            config="lhcb", 
            polarity="magdown", 
            eventtype="94000000", 
            datatype="2024", 
            filetype="ftuple.root", 
            name = "data_24_magdown_24c4a", 
            version = "v1r3175"
            )[:],

        "25_up_c1": datasets(
            config="lhcb", 
            polarity="magup", 
            eventtype="94000000", 
            datatype="2025", 
            filetype="ftuple.root", 
            name = "data_25_magup_25c1", 
            version = "v1r3441"
            )[:],
        "25_down_c1": datasets(
            config="lhcb", 
            polarity="magdown", 
            eventtype="94000000", 
            datatype="2025", 
            filetype="ftuple.root", 
            name = "data_25_magdown_25c1", 
            version = "v1r3441"
            )[:],
        # "25_down_c2": datasets(
        #     config="lhcb", 
        #     polarity="magdown", 
        #     eventtype="94000000", 
        #     datatype="2025", 
        #     filetype="ftuple.root", 
        #     name = "data_25_magdown_25c2", 
        #     version = "v1r3441"
        #     )[:],
    }

