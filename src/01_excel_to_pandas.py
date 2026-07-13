import pandas as pd

file_path = "reports/excel/synthetic_credit_risk_prototype.xlsx"

df = pd.read_excel(
    file_path,
    usecols="A:H",
    nrows=6
)

print("Applicant data:")
print(df)

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nPython KPI summary:")

average_income = df["Income"].mean()
default_rate = df["Defaulted"].mean()
high_risk_count = (df["Risk_Flag"] == "High").sum()

print("Average income:", round(average_income, 2))
print("Default rate:", round(default_rate, 2))
print("High risk count:", high_risk_count)

print("\nDecision count:")

decision_count = df["Decision"].value_counts()

print(decision_count)

print("\nHigh risk applicants:")

high_risk_applicants = df[df["Risk_Flag"] == "High"]

print(high_risk_applicants[["Applicant_ID", "Credit_Score", "Debt_to_Income", "Decision"]])

output_path = "reports/excel/high_risk_applicants.csv"

high_risk_applicants.to_csv(output_path, index=False)

print("\nSaved high risk applicants to:", output_path)