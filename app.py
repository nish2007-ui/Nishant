"""
app.py
Loan Default Risk Predictor - Streamlit web tool with 3 tiers:
Basic (self-reported only), Moderate (+ light credit info),
Advanced (+ full credit bureau detail).

Run with: streamlit run app.py
Requires model_<tier>.pkl, scaler_<tier>.pkl, features_<tier>.pkl
for tier in {basic, moderate, advanced} (created by train_model.py)
"""

import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------------
# Page setup
# ---------------------------------------------------------
st.set_page_config(page_title="Loan Default Risk Predictor", page_icon="💰", layout="centered")

st.title("💰 Loan Default Risk Predictor")
st.write(
    "Estimate the probability that a loan applicant will default. "
    "Choose how much information you want to provide — more detail "
    "generally gives a more accurate estimate."
)
st.info(
    "This is a demo/educational tool built on historical LendingClub data. "
    "It should not be used for real lending decisions.",
    icon="ℹ️",
)

# ---------------------------------------------------------
# Tier metadata
# ---------------------------------------------------------
TIER_INFO = {
    "Basic": {
        "key": "basic",
        "desc": "Only info a borrower knows off the top of their head. No credit report needed.",
    },
    "Moderate": {
        "key": "moderate",
        "desc": "Adds a few common credit details (FICO score, credit utilization, account counts).",
    },
    "Advanced": {
        "key": "advanced",
        "desc": "Adds full credit bureau detail (delinquencies, inquiries, public records, account history). Most accurate, but requires a credit report.",
    },
}

# ---------------------------------------------------------
# Load model artifacts for a given tier
# ---------------------------------------------------------
@st.cache_resource
def load_artifacts(tier_key):
    model = joblib.load(f"model_{tier_key}.pkl")
    scaler = joblib.load(f"scaler_{tier_key}.pkl")
    features = joblib.load(f"features_{tier_key}.pkl")
    return model, scaler, features

# ---------------------------------------------------------
# Tier selector
# ---------------------------------------------------------
tier_choice = st.radio(
    "Select level of detail",
    options=list(TIER_INFO.keys()),
    horizontal=True,
)
tier_key = TIER_INFO[tier_choice]["key"]
st.caption(TIER_INFO[tier_choice]["desc"])

try:
    model, scaler, FEATURES = load_artifacts(tier_key)
except FileNotFoundError:
    st.error(
        f"Model files for '{tier_choice}' not found. Run `python train_model.py` "
        f"first to generate model_{tier_key}.pkl, scaler_{tier_key}.pkl, "
        f"features_{tier_key}.pkl in this folder."
    )
    st.stop()

st.caption(f"This tier uses **{len(FEATURES)} features**.")

with st.sidebar:
    st.header("About this model")
    st.write(
        "- Trained on historical LendingClub accepted loans\n"
        "- Logistic Regression with balanced class weights\n"
        "- Three tiers trade off ease-of-use vs. accuracy:"
    )
    for name, info in TIER_INFO.items():
        st.write(f"**{name}** — {info['desc']}")

# ---------------------------------------------------------
# Input form (fields shown depend on selected tier)
# ---------------------------------------------------------
with st.form("loan_form"):
    st.subheader("Loan Details")
    col1, col2 = st.columns(2)
    with col1:
        loan_amnt = st.number_input(
            "Loan amount requested ($)", min_value=500, max_value=100000, value=10000, step=500
        )
    with col2:
        term = st.selectbox("Loan term (months)", [36, 60])

    st.subheader("Borrower Details")
    col3, col4 = st.columns(2)
    with col3:
        annual_inc = st.number_input(
            "Annual income ($)", min_value=0, max_value=2000000, value=60000, step=1000
        )
        dti = st.number_input(
            "Debt-to-income ratio (%)", min_value=0.0, max_value=100.0, value=15.0, step=0.5,
            help="Total monthly debt payments divided by monthly income, as a percentage."
        )
    with col4:
        emp_length = st.slider("Years employed", 0, 10, 3, help="10 = 10+ years")
        credit_history_years = st.number_input(
            "Years of credit history", min_value=0.0, max_value=60.0, value=8.0, step=0.5
        )

    verification_status = st.selectbox(
        "Income verification status",
        options=[0, 1, 2],
        format_func=lambda x: {0: "Not Verified", 1: "Source Verified", 2: "Verified"}[x],
    )
    home_ownership = st.selectbox("Home ownership", ["RENT", "MORTGAGE", "OWN", "ANY"])
    purpose = st.selectbox("Loan purpose", ["debt_consolidation", "credit_card", "Other"])

    moderate_vals = {}
    advanced_vals = {}

    if tier_key in ("moderate", "advanced"):
        st.subheader("Credit Details")
        col5, col6 = st.columns(2)
        with col5:
            moderate_vals["fico_range_low"] = st.number_input(
                "FICO score (lower bound)", min_value=300, max_value=850, value=680, step=5
            )
            moderate_vals["revol_util"] = st.number_input(
                "Revolving credit utilization (%)", min_value=0.0, max_value=150.0, value=30.0, step=1.0,
                help="Credit card balance divided by credit limit, as a percentage."
            )
            moderate_vals["revol_bal"] = st.number_input(
                "Revolving credit balance ($)", min_value=0, max_value=500000, value=8000, step=500
            )
        with col6:
            moderate_vals["open_acc"] = st.number_input(
                "Number of open credit accounts", min_value=0, max_value=100, value=8, step=1
            )
            moderate_vals["total_acc"] = st.number_input(
                "Total credit accounts (ever)", min_value=0, max_value=150, value=20, step=1
            )
            moderate_vals["mort_acc"] = st.number_input(
                "Number of mortgage accounts", min_value=0, max_value=20, value=1, step=1
            )

    if tier_key == "advanced":
        st.subheader("Full Credit History (Advanced)")
        col7, col8 = st.columns(2)
        with col7:
            advanced_vals["delinq_2yrs"] = st.number_input(
                "30+ day late payments (last 2 years)", min_value=0, max_value=30, value=0, step=1
            )
            advanced_vals["inq_last_6mths"] = st.number_input(
                "Credit inquiries (last 6 months)", min_value=0, max_value=20, value=1, step=1
            )
            advanced_vals["pub_rec"] = st.number_input(
                "Public derogatory records", min_value=0, max_value=20, value=0, step=1
            )
            advanced_vals["collections_12_mths_ex_med"] = st.number_input(
                "Collections (last 12 months, non-medical)", min_value=0, max_value=20, value=0, step=1
            )
            advanced_vals["acc_now_delinq"] = st.number_input(
                "Accounts currently delinquent", min_value=0, max_value=20, value=0, step=1
            )
            advanced_vals["tot_coll_amt"] = st.number_input(
                "Total amount in collections ($)", min_value=0, max_value=500000, value=0, step=100
            )
            advanced_vals["chargeoff_within_12_mths"] = st.number_input(
                "Charge-offs (last 12 months)", min_value=0, max_value=20, value=0, step=1
            )
        with col8:
            advanced_vals["tot_cur_bal"] = st.number_input(
                "Total current balance, all accounts ($)", min_value=0, max_value=2000000, value=50000, step=1000
            )
            advanced_vals["acc_open_past_24mths"] = st.number_input(
                "Accounts opened (last 24 months)", min_value=0, max_value=30, value=2, step=1
            )
            advanced_vals["mo_sin_old_rev_tl_op"] = st.number_input(
                "Months since oldest revolving account opened", min_value=0, max_value=800, value=150, step=1
            )
            advanced_vals["mo_sin_rcnt_tl"] = st.number_input(
                "Months since most recent account opened", min_value=0, max_value=400, value=8, step=1
            )
            advanced_vals["num_tl_op_past_12m"] = st.number_input(
                "Accounts opened (last 12 months)", min_value=0, max_value=20, value=1, step=1
            )
            advanced_vals["pub_rec_bankruptcies"] = st.number_input(
                "Public bankruptcy records", min_value=0, max_value=10, value=0, step=1
            )
            advanced_vals["total_bc_limit"] = st.number_input(
                "Total bankcard credit limit ($)", min_value=0, max_value=500000, value=15000, step=500
            )

    submitted = st.form_submit_button("Predict Default Risk", use_container_width=True)

# ---------------------------------------------------------
# Build feature row + predict
# ---------------------------------------------------------
if submitted:
    row = {f: 0 for f in FEATURES}

    row["loan_amnt"] = loan_amnt
    row["term"] = term
    row["emp_length"] = emp_length
    row["annual_inc"] = annual_inc
    row["dti"] = dti
    row["credit_history_years"] = credit_history_years
    row["verification_status"] = verification_status

    home_col = f"home_ownership_{home_ownership}"
    if home_col in row:
        row[home_col] = 1

    purpose_col = f"purpose_{purpose}"
    if purpose_col in row:
        row[purpose_col] = 1

    for k, v in moderate_vals.items():
        if k in row:
            row[k] = v
    for k, v in advanced_vals.items():
        if k in row:
            row[k] = v

    X_input = pd.DataFrame([row])[FEATURES]
    X_scaled = scaler.transform(X_input)

    proba = model.predict_proba(X_scaled)[0][1]
    prediction = model.predict(X_scaled)[0]

    st.divider()
    st.subheader("Result")

    c1, c2 = st.columns(2)
    with c1:
        st.metric("Estimated default probability", f"{proba * 100:.1f}%")
    with c2:
        if proba < 0.30:
            st.success("✅ Lower risk of default")
        elif proba < 0.55:
            st.warning("🟡 Medium risk of default")
        else:
            st.error("⚠️ Higher risk of default")

    st.progress(min(proba, 1.0))

    st.caption(
        f"Prediction based on the **{tier_choice}** model "
        f"({len(FEATURES)} features), trained on historical LendingClub data. "
        "Real lending decisions rely on full credit reports and additional "
        "underwriting criteria not captured here."
    )
