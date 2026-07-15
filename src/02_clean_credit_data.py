import pandas as pd

file_path = "reports/excel/synthetic_credit_risk_prototype.xlsx"

df = pd.read_excel(
    file_path,
    usecols="A:H",
    nrows=6
)

print("Original data:")
print(df)

print("\nMissing values by column:")

missing_values = df.isna().sum()

print(missing_values)

print("\nDebt level:")

df["Debt_Level"] = pd.cut(
    df["Debt_to_Income"],
    bins=[0, 0.3, 0.5, 1],
    labels=["Low", "Medium", "High"]
)

print(df[["Applicant_ID", "Debt_to_Income", "Debt_Level"]])

print("\nApplicants sorted by debt-to-income:")

sorted_df = df.sort_values(
    by="Debt_to_Income",
    ascending=False
)

print(sorted_df[["Applicant_ID", "Debt_to_Income", "Risk_Flag", "Decision"]])

output_path = "data/processed/clean_credit_applicants.csv"

df.to_csv(output_path, index=False)

print("\nSaved cleaned data to:", output_path)