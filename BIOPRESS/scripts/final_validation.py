
import pandas as pd

# 1. Load datasets
df = pd.read_csv("data/modeling_dataset.csv")
clean_df = pd.read_csv("data/hand_hygiene_data_cleaned.csv")

print("\nFINAL DATA VALIDATION")

# 2. Expected columns
expected_columns = [
    "Ward",
    "Profcat",
    "Shift",
    "Indication",
    "Complied"
]

# 3. Expected categories from the dataset
expected_shifts = {"Morning", "Afternoon", "Night"}
expected_targets = {"No", "Yes"}

# 4. Validation checks
checks = {
    "917 Records": len(df) == 917,
    "5 Columns": len(df.columns) == 5,
    "Correct Columns": df.columns.tolist() == expected_columns,
    "No Missing Values": df.isnull().sum().sum() == 0,
    "No Duplicate Rows in Source": clean_df.duplicated().sum() == 0,
    "Correct Target Classes": set(df["Complied"].unique()) == expected_targets,
    "Valid Shift Values": set(df["Shift"].unique()) == expected_shifts,
    "Modeling Rows Match Source": len(df) == len(clean_df)
}

print("\nFINAL CHECK RESULTS")

for check, result in checks.items():
    print(check, ":", "PASS" if result else "FAIL")

print("\nModeling Dataset Duplicates:", df.duplicated().sum())

print("\nOverall Result:",
      "ALL CHECKS PASSED" if all(checks.values())
      else "SOME CHECKS FAILED")
