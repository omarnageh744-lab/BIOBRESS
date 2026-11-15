
import pandas as pd

# 1. Load cleaned dataset
df = pd.read_csv("data/hand_hygiene_data_cleaned.csv")

# 2. Select approved features and target
selected_columns = [
    "Ward",
    "Profcat",
    "Shift",
    "Indication",
    "Complied"
]

model_df = df[selected_columns].copy()

# 3. Validate the prepared dataset
print("\nFEATURE PREPARATION VALIDATION")

print("Rows:", len(model_df))
print("Columns:", len(model_df.columns))

print("\nSelected Columns:")
print(model_df.columns.tolist())

print("\nMissing Values:")
print(model_df.isnull().sum())

print("\nTarget Distribution:")
print(model_df["Complied"].value_counts())

# 4. Save prepared dataset
model_df.to_csv("data/modeling_dataset.csv", index=False)

print("\nModeling dataset saved successfully!")
