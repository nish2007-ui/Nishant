"""
app.py
Loan Default Risk Predictor - Streamlit web tool.

Run with: streamlit run app.py
Requires model.pkl, scaler.pkl, features.pkl (created by train_model.py)
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
    "Estimate the probability that a loan applicant will default, "
    "based on information a typical applicant can provide themselves."
)
st.info(
    "This is a demo/educational tool built on historical LendingClub data. "
    "It should not be used for real lending decisions.",
    icon="ℹ️",
)

# ---------------------------------------------------------
# Load model artifacts
# ---------------------------------------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    features = joblib.load("features.pkl")
    return model, scaler, features

try:
    model, scaler, FEATURES = load_artifacts()
except FileNotFoundError:
    st.error(
        "Model files not found. Run `python train_model.py` first to generate "
        "model.pkl, scaler.pkl, and features.pkl in this folder."
    )
    st.stop()

# ---------------------------------------------------------
# Sidebar: model info
# ---------------------------------------------------------
with st.sidebar:
    st.header("About this model")
    st.write(
        "- Trained on historical LendingClub accepted loans\n"
        "- Uses only applicant-friendly features (no credit bureau pull required)\n"
        "- Model: Logistic Regression with balanced class weights"
    )
    st.caption(
        "Because only self-reportable features are used, accuracy is lower than "
        "a full underwriting model — this trades some precision for usability."
    )

# ---------------------------------------------------------
# User input form
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
        if prediction == 1:
            st.error("⚠️ Higher risk of default")
        else:
            st.success("✅ Lower risk of default")

    st.progress(min(proba, 1.0))

    st.caption(
        "Prediction based on a simplified model trained on historical LendingClub "
        "data. Real lending decisions rely on full credit reports and additional "
        "underwriting criteria not captured here."
    )
