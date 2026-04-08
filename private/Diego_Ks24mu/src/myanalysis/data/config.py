variables_mc_1= [ 
    "KS_M",
    "L1_PID_MU", "L2_PID_MU", "L3_PID_MU", "L4_PID_MU",
    "L1_ISMUON", "L2_ISMUON", "L3_ISMUON", "L4_ISMUON", 
    "KS_TRUEID", 
    "L1_TRUEID", "L2_TRUEID", "L3_TRUEID", "L4_TRUEID",
    "L1_MC_MOTHER_KEY", "L2_MC_MOTHER_KEY", "L3_MC_MOTHER_KEY", "L4_MC_MOTHER_KEY",
    "L1_MC_MOTHER_ID", "L2_MC_MOTHER_ID", "L3_MC_MOTHER_ID", "L4_MC_MOTHER_ID",
    "L1_PROBNN_MU", "L2_PROBNN_MU", "L3_PROBNN_MU", "L4_PROBNN_MU",
    "KS_Hlt1DiMuonSoftDecision_TOS"
]

variables_data = [
    "EVENTNUMBER", 
    "KS_Hlt1DiMuonSoftDecision_TOS",
    # "Hlt1DiMuonSoftDecision", , "L1_Hlt1DiMuonSoftDecision_TOS", "L2_Hlt1DiMuonSoftDecision_TOS", "L3_Hlt1DiMuonSoftDecision_TOS", "L4_Hlt1DiMuonSoftDecision_TOS",
    "KS_M", "KS_MAXSDOCA", "KS_MAXSDOCACHI2", "KS_BPVDIRA", "KS_BPVIP", "KS_BPVIPCHI2", "KS_BPVFD", "KS_BPVFDCHI2", "KS_BPVCHI2DOF", "KS_BPVX", "KS_BPVY", "KS_BPVLTIME", "KS_BPVVDZ", 
    "L1_M", "L1_PX", "L1_PY", "L1_PZ", "L1_PT", "L1_P", "L1_TX", "L1_TY", "L1_ISMUON", "L1_TRCHI2DOF", "L1_TRGHOSTPROB", "L1_PROBNN_GHOST", "L1_RICH_DLL_MU", "L1_PID_MU", "L1_PROBNN_MU", 
    "L2_M", "L2_PX", "L2_PY", "L2_PZ", "L2_PT", "L2_P", "L2_TX", "L2_TY", "L2_ISMUON", "L2_TRCHI2DOF", "L2_TRGHOSTPROB", "L2_PROBNN_GHOST", "L2_RICH_DLL_MU", "L2_PID_MU", "L2_PROBNN_MU",
    "L3_M", "L3_PX", "L3_PY", "L3_PZ", "L3_PT", "L3_P", "L3_TX", "L3_TY", "L3_ISMUON", "L3_TRCHI2DOF", "L3_TRGHOSTPROB", "L3_PROBNN_GHOST", "L3_RICH_DLL_MU", "L3_PID_MU", "L3_PROBNN_MU",
    "L4_M", "L4_PX", "L4_PY", "L4_PZ", "L4_PT", "L4_P", "L4_TX", "L4_TY", "L4_ISMUON", "L4_TRCHI2DOF", "L4_TRGHOSTPROB", "L4_PROBNN_GHOST", "L4_RICH_DLL_MU", "L4_PID_MU", "L4_PROBNN_MU",
    # Featuresdf_24c2_up
    "L1_BPVIP", "L1_BPVIPCHI2",  
    "L2_BPVIP", "L2_BPVIPCHI2", 
    "L3_BPVIP", "L3_BPVIPCHI2", 
    "L4_BPVIP", "L4_BPVIPCHI2",
    # To obtain VeloMatterVito
    "KS_END_VX", "KS_END_VY", "KS_END_VZ", "KS_END_VXERR", "KS_END_VYERR", "KS_END_VZERR", "KS_ENDVERTEX_CHI2DOF", "KS_BPVVDRHO",  "RUNNUMBER"
    ]

variables_mc_2= [ 
    "KS_M", "KS_MAXSDOCA", "KS_MAXSDOCACHI2", "KS_BPVDIRA", "KS_BPVIP", "KS_BPVIPCHI2", "KS_BPVFD", "KS_BPVFDCHI2", "KS_BPVCHI2DOF", "KS_BPVX", "KS_BPVY", "KS_BPVLTIME", "KS_BPVVDZ", 
    "KS_TRUEID", 
    "L1_TRUEID", "L2_TRUEID", "L3_TRUEID", "L4_TRUEID",
    "L1_MC_MOTHER_KEY", "L2_MC_MOTHER_KEY", "L3_MC_MOTHER_KEY", "L4_MC_MOTHER_KEY",
    "L1_MC_MOTHER_ID", "L2_MC_MOTHER_ID", "L3_MC_MOTHER_ID", "L4_MC_MOTHER_ID",
    "KS_Hlt1DiMuonSoftDecision_TOS",
    "L1_M", "L1_PX", "L1_PY", "L1_PZ", "L1_PT", "L1_P", "L1_TX", "L1_TY", "L1_ISMUON", "L1_TRCHI2DOF", "L1_TRGHOSTPROB", "L1_PROBNN_GHOST", "L1_RICH_DLL_MU", "L1_PID_MU", "L1_PROBNN_MU", 
    "L2_M", "L2_PX", "L2_PY", "L2_PZ", "L2_PT", "L2_P", "L2_TX", "L2_TY", "L2_ISMUON", "L2_TRCHI2DOF", "L2_TRGHOSTPROB", "L2_PROBNN_GHOST", "L2_RICH_DLL_MU", "L2_PID_MU", "L2_PROBNN_MU",
    "L3_M", "L3_PX", "L3_PY", "L3_PZ", "L3_PT", "L3_P", "L3_TX", "L3_TY", "L3_ISMUON", "L3_TRCHI2DOF", "L3_TRGHOSTPROB", "L3_PROBNN_GHOST", "L3_RICH_DLL_MU", "L3_PID_MU", "L3_PROBNN_MU",
    "L4_M", "L4_PX", "L4_PY", "L4_PZ", "L4_PT", "L4_P", "L4_TX", "L4_TY", "L4_ISMUON", "L4_TRCHI2DOF", "L4_TRGHOSTPROB", "L4_PROBNN_GHOST", "L4_RICH_DLL_MU", "L4_PID_MU", "L4_PROBNN_MU",
    "L1_BPVIP", "L1_BPVIPCHI2",  
    "L2_BPVIP", "L2_BPVIPCHI2", 
    "L3_BPVIP", "L3_BPVIPCHI2", 
    "L4_BPVIP", "L4_BPVIPCHI2",
    "KS_END_VX", "KS_END_VY", "KS_END_VZ", "KS_END_VXERR", "KS_END_VYERR", "KS_END_VZERR", "KS_ENDVERTEX_CHI2DOF", "KS_BPVVDRHO",  "RUNNUMBER"
]

# versions = ["40_42","37_39","35_37","31_34"]
# types = ["MC","Reco","Loose"]

# mc_trees = {
#     "MC": "MCKs4mu/DecayTree",
#     "Reco": "RecoKs4mu/DecayTree",
#     "Loose": "Hlt2RD_KS0ToMuMuMuMu_Loose/DecayTree"
# }

# data_trees = {
#     "DATA": "Hlt2RD_KS0ToMuMuMuMu_Loose/DecayTree"
# }

mc_config = {
    "MC": {
        "tree": "MCKs4mu/DecayTree",
        "vars": ["KS_M"],
        "add_angles": False,
        "sideband": False
    },
    "Reco": {
        "tree": "RecoKs4mu/DecayTree",
        "vars": variables_mc_1,
        "add_angles": False,
        "sideband": False
    },
    "Loose": {
        "tree": "Hlt2RD_KS0ToMuMuMuMu_Loose/DecayTree",
        "vars": variables_mc_2,
        "add_angles": True,
        "sideband": False   
    }
}

data_config = {
    "DATA": {
        "tree": "Hlt2RD_KS0ToMuMuMuMu_Loose/DecayTree",
        "vars": variables_data,
        "add_angles": True,
        "sideband": True   
    }
}