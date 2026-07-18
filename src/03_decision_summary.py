import pandas as pd

file_path = "data/processed/clean_credit_applicants.csv"

df = pd.read_csv(file_path)

print("Cleaned applicant data:")
print(df)

print("\nDecision summary:")

decision_summary = df.groupby("Decision").agg(
    applicant_count=("Applicant_ID", "count"),
    average_credit_score=("Credit_Score", "mean"),
    average_dti=("Debt_to_Income", "mean")
).reset_index()

print(decision_summary)

decision_summary["average_credit_score"] = decision_summary["average_credit_score"].round(2)
decision_summary["average_dti"] = decision_summary["average_dti"].round(3)

output_path = "reports/excel/decision_summary.csv"

decision_summary.to_csv(output_path, index=False)

print("\nSaved decision summary to:", output_path)