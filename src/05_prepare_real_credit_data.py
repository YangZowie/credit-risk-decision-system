import pandas as pd

input_path = "data/raw/SouthGermanCredit.asc"

df = pd.read_csv(input_path, sep=" ")

df = df.rename(columns={
    "laufkont": "checking_account_status",
    "laufzeit": "duration_months",
    "moral": "credit_history",
    "verw": "purpose",
    "hoehe": "loan_amount",
    "sparkont": "savings_account_status",
    "beszeit": "employment_duration",
    "rate": "installment_rate",
    "famges": "personal_status_sex",
    "buerge": "other_debtors",
    "wohnzeit": "present_residence_years",
    "verm": "property",
    "alter": "age",
    "weitkred": "other_installment_plans",
    "wohn": "housing",
    "bishkred": "existing_credits",
    "beruf": "job",
    "pers": "people_liable",
    "telef": "telephone",
    "gastarb": "foreign_worker",
    "kredit": "credit_risk"
})

print("Prepared real credit data preview:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values by column:")
print(df.isna().sum())

print("\nCredit risk distribution:")
print(df["credit_risk"].value_counts())

output_path = "data/processed/south_german_credit_clean.csv"

df.to_csv(output_path, index=False)

print("\nSaved prepared real credit data to:", output_path)