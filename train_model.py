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
# 3. Select ONLY user-friendly (Tier 1) features
# ---------------------------------------------------------
FEATURES = [
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
FEATURES = [f for f in FEATURES if f in df.columns]

X = df[FEATURES].copy()
y = df["target"]
X = X.fillna(X.median(numeric_only=True))

# ---------------------------------------------------------
# 4. Train / test split
# ---------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---------------------------------------------------------
# 5. Scale + train
# ---------------------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

# ---------------------------------------------------------
# 6. Evaluate
# ---------------------------------------------------------
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1]

print("\nF1 score (default class):", round(f1_score(y_test, y_pred), 3))
print("ROC-AUC:", round(roc_auc_score(y_test, y_proba), 3))
print(classification_report(y_test, y_pred, target_names=["Fully Paid", "Default"]))

# ---------------------------------------------------------
# 7. Save artifacts for the Streamlit app
# ---------------------------------------------------------
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(FEATURES, "features.pkl")
print("\nSaved model.pkl, scaler.pkl, features.pkl")
