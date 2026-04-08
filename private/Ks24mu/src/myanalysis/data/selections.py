def muon_filter(df):

    mask = (
        (df["L1_ISMUON"] == 1) &
        (df["L2_ISMUON"] == 1) &
        (df["L3_ISMUON"] == 1) &
        (df["L4_ISMUON"] == 1) 
    )

    df_final = df[mask].copy()

    return df_final


def PID_filter(df,l1,l2,l3,l4):

    mask = (
        (df["L1_PID_MU"] > l1) &
        (df["L2_PID_MU"] > l2) &
        (df["L3_PID_MU"] > l3) &
        (df["L4_PID_MU"] > l4)
    )

    df_final = df[mask].copy()

    return df_final

def truth_matching(df):

    mask = (
        (df['KS_TRUEID'] == 310) &
        (df['L1_TRUEID'] == -13) &
        (df['L2_TRUEID'] == -13) &
        (df['L3_TRUEID'] == 13) &
        (df['L4_TRUEID'] == 13) &
        (df['L1_MC_MOTHER_KEY'] == df['L2_MC_MOTHER_KEY']) &
        (df['L1_MC_MOTHER_KEY'] == df['L3_MC_MOTHER_KEY']) &
        (df['L1_MC_MOTHER_KEY'] == df['L4_MC_MOTHER_KEY']) &
        (df['L1_MC_MOTHER_ID'] == 310) &
        (df['L2_MC_MOTHER_ID'] == 310) &
        (df['L3_MC_MOTHER_ID'] == 310) &
        (df['L4_MC_MOTHER_ID'] == 310)
    )

    df_final = df[mask].copy()

    return df_final

def dimuon_filter(df):

    mask = (
        (df["KS_Hlt1DiMuonSoftDecision_TOS"] == 1)
    )

    df_final = df[mask].copy()

    return df_final

def probNN_filter(df):

    mask = (
        # (df["L1_PROBNN_MU"] > 0) &
        # (df["L2_PROBNN_MU"] > 0) &
        # (df["L3_PROBNN_MU"] > 0) &
        (df["L1_PROBNN_MU"] > 0.1) 
    )

    df_final = df[mask].copy()

    return df_final

def probNN_filter_v2(df,c):

    mask = (
        (df["L1_PROBNN_MU"] > c) 
    )

    df_final = df[mask].copy()

    return df_final

def angle_filter(df,c):

    mask = (
        (df["L1_P"] > 3) &
        (df["theta_13"] > c) &
        (df["theta_14"] > c) &
        (df["theta_23"] > c) &
        (df["theta_24"] > c) &
        (df["theta_34"] > c) 
    )

    df_final = df[mask].copy()

    return df_final

def normalize(df):

    # =========================
    # Hijas
    # =========================
    for i in [1, 2, 3, 4]:
        df = df[df[f"L{i}_P"] > 3000]          # MeV
        df = df[df[f"L{i}_PT"] > 80]           # MeV
        df = df[df[f"L{i}_TRCHI2DOF"] < 9]
        df = df[df[f"L{i}_BPVIP"] > 1]         # mm
        df = df[df[f"L{i}_BPVIPCHI2"] > 25]
        df = df[df[f"L{i}_PID_MU"] > -3]
        df = df[df[f"L{i}_ISMUON"] == 1]

    # =========================
    # Madre
    # =========================
    df = df[
        (df["KS_BPVDIRA"] > 0.999) &
        (df["KS_BPVCHI2DOF"] < 9) &
        (df["KS_MAXSDOCA"] < 0.2) &
        (df["KS_MAXSDOCACHI2"] < 16) &
        (df["KS_BPVFD"] > 3) &
        (df["KS_BPVIP"] < 0.4) &
        (df["KS_BPVIPCHI2"] < 25) &
        (df["KS_BPVLTIME"] > 4.5) &
        (df["KS_M"] > 470) & (df["KS_M"] < 600)
    ]

    return df