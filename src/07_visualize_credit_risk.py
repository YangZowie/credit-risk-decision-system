import pandas as pd
import matplotlib.pyplot as plt

file_path = "reports/eda/credit_risk_summary.csv"

summary = pd.read_csv(file_path)

print("EDA summary:")
print(summary)

summary["credit_risk_label"] = summary["credit_risk"].map({
    0: "Bad Credit",
    1: "Good Credit"
})

plt.figure(figsize=(7, 5))

plt.bar(
    summary["credit_risk_label"],
    summary["average_loan_amount"]
)

plt.title("Average Loan Amount by Credit Risk")
plt.xlabel("Credit Risk")
plt.ylabel("Average Loan Amount")
plt.tight_layout()

output_path = "reports/eda/average_loan_amount_by_credit_risk.png"

plt.savefig(output_path)

print("\nSaved chart to:", output_path)

plt.figure(figsize=(7, 5))

plt.bar(
    summary["credit_risk_label"],
    summary["average_duration_months"]
)

plt.title("Average Loan Duration by Credit Risk")
plt.xlabel("Credit Risk")
plt.ylabel("Average Duration (Months)")
plt.tight_layout()

output_path = "reports/eda/average_duration_by_credit_risk.png"

plt.savefig(output_path)

print("Saved chart to:", output_path)