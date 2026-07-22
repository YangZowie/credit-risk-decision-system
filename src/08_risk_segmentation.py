import pandas as pd

file_path = "data/processed/south_german_credit_clean.csv"

df = pd.read_csv(file_path)

print("Real credit data:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

df["loan_amount_segment"] = pd.cut(
    df["loan_amount"],
    bins=[0, 2000, 5000, df["loan_amount"].max()],
    labels=["Low Amount", "Medium Amount", "High Amount"]
)

print("\nLoan amount segment count:")
print(df["loan_amount_segment"].value_counts())

df["bad_credit"] = 1 - df["credit_risk"]

print("\nBad credit rate by loan amount segment:")

amount_segment_summary = df.groupby("loan_amount_segment").agg(
    applicant_count=("bad_credit", "count"),
    bad_credit_rate=("bad_credit", "mean"),
    average_loan_amount=("loan_amount", "mean")
).round(3).reset_index()

print(amount_segment_summary)

df["duration_segment"] = pd.cut(
    df["duration_months"],
    bins=[0, 12, 24, df["duration_months"].max()],
    labels=["Short Term", "Medium Term", "Long Term"]
)

print("\nBad credit rate by duration segment:")

duration_segment_summary = df.groupby("duration_segment").agg(
    applicant_count=("bad_credit", "count"),
    bad_credit_rate=("bad_credit", "mean"),
    average_duration_months=("duration_months", "mean")
).round(3).reset_index()

print(duration_segment_summary)

amount_output_path = "reports/eda/loan_amount_segment_summary.csv"
duration_output_path = "reports/eda/duration_segment_summary.csv"

amount_segment_summary.to_csv(amount_output_path, index=False)
duration_segment_summary.to_csv(duration_output_path, index=False)

print("\nSaved amount segment summary to:", amount_output_path)
print("Saved duration segment summary to:", duration_output_path)