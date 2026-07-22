import pandas as pd

file_path = "data/processed/south_german_credit_clean.csv"

df = pd.read_csv(file_path)

print("Real credit dataset:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nCredit risk count:")

risk_count = df["credit_risk"].value_counts()

print(risk_count)

print("\nCredit risk rate:")

risk_rate = df["credit_risk"].value_counts(normalize=True).round(3)

print(risk_rate)

print("\nAverage loan amount by credit risk:")

loan_amount_by_risk = df.groupby("credit_risk")["loan_amount"].mean().round(2)

print(loan_amount_by_risk)

print("\nAverage duration by credit risk:")

duration_by_risk = df.groupby("credit_risk")["duration_months"].mean().round(2)

print(duration_by_risk)

print("\nCredit risk summary table:")

summary_table = df.groupby("credit_risk").agg(
    applicant_count=("credit_risk", "count"),
    average_loan_amount=("loan_amount", "mean"),
    average_duration_months=("duration_months", "mean"),
    average_age=("age", "mean")
).round(2).reset_index()

print(summary_table)

output_path = "reports/eda/credit_risk_summary.csv"

summary_table.to_csv(output_path, index=False)

print("\nSaved EDA summary to:", output_path)