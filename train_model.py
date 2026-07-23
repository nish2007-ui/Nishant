"""
train_model.py
Trains a "lite" loan default model using only user-answerable features,
from the corrected Loan_Default.csv (loan_status: 1 = Fully Paid, 0 = Charged Off).

Saves model.pkl, scaler.pkl, features.pkl for the Streamlit app (app.py).
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score, roc_auc_score, classification_report
import joblib

# ---------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------
df = pd.read_csv("Loan_Default.csv")

# ---------------------------------------------------------
# 2. Flip target so 1 = Default (more intuitive for the app)
#    Original: loan_status = 1 -> Fully Paid, 0 -> Charged Off
# ---------------------------------------------------------
df["target"] = 1 - df["loan_status"]
df = df.drop(columns=["loan_status"])

print("Target distribution (1 = Default):")
print(df["target"].value_counts(normalize=True).round(3))

# ---------------------------------------------------------
# 3. Define three feature tiers (each builds on the last)
# ---------------------------------------------------------
BASIC_FEATURES = [
    "loan_amnt",
    "term",
    "emp_length",
    "annual_inc",
    "dti",
    "credit_history_years",
    "verification_status",
    "home_ownership_MORTGAGE",
    "home_ownership_OWN",
    "home_ownership_RENT",
    "home_ownership_ANY",
    "purpose_credit_card",
    "purpose_debt_consolidation",
    "purpose_Other",
]

MODERATE_FEATURES = BASIC_FEATURES + [
    "fico_range_low",
    "revol_util",
    "revol_bal",
    "open_acc",
    "total_acc",
    "mort_acc",
]

ADVANCED_FEATURES = MODERATE_FEATURES + [
    "delinq_2yrs",
    "inq_last_6mths",
    "pub_rec",
    "collections_12_mths_ex_med",
    "acc_now_delinq",
    "tot_coll_amt",
    "tot_cur_bal",
    "acc_open_past_24mths",
    "chargeoff_within_12_mths",
    "mo_sin_old_rev_tl_op",
    "mo_sin_rcnt_tl",
    "num_tl_op_past_12m",
    "pub_rec_bankruptcies",
    "total_bc_limit",
]

TIERS = {
    "basic": BASIC_FEATURES,
    "moderate": MODERATE_FEATURES,
    "advanced": ADVANCED_FEATURES,
}

# ---------------------------------------------------------
# 4. Train, evaluate, and save one model per tier
# ---------------------------------------------------------
for tier_name, feature_list in TIERS.items():
    feature_list = [f for f in feature_list if f in df.columns]

    X = df[feature_list].copy()
    y = df["target"]
    X = X.fillna(X.median(numeric_only=True))

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    y_proba = model.predict_proba(X_test_scaled)[:, 1]

    print(f"\n=== {tier_name.upper()} ({len(feature_list)} features) ===")
    print("F1 score (default class):", round(f1_score(y_test, y_pred), 3))
    print("ROC-AUC:", round(roc_auc_score(y_test, y_proba), 3))
    print(classification_report(y_test, y_pred, target_names=["Fully Paid", "Default"]))

    joblib.dump(model, f"model_{tier_name}.pkl")
    joblib.dump(scaler, f"scaler_{tier_name}.pkl")
    joblib.dump(feature_list, f"features_{tier_name}.pkl")

print("\nSaved model/scaler/features .pkl files for: basic, moderate, advanced")
