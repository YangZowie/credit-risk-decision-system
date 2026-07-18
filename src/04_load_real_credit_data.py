import pandas as pd

file_path = "data/raw/SouthGermanCredit.asc"

df = pd.read_csv(file_path, sep=" ")

print("Real credit data preview:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nTarget variable distribution:")

target_distribution = df["kredit"].value_counts()

print(target_distribution)