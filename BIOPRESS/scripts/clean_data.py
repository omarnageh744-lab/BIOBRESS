import pandas as pd  
#1.Load original dataset
df=pd.read_csv("data/hand_hygiene_data_labeled.csv")

#2. create a copy
clean_df=df.copy()

#3. Standrdize Shift category
clean_df["Shift"]=clean_df["Shift"].replace({
    "After noon":"Afternoon"
})

#4. Check the result
print("Original Shift values:")
print(df["Shift"].value_counts())

print("\nCleaned Shift values:")
print(clean_df["Shift"].value_counts())

#5. Save cleaned dataset
clean_df.to_csv(
    "data/hand_hygiene_data_cleaned.csv",
    index=False
)
print("\nCleaned dataset saved successfully!")

#6. Check cleaned dataset
print("\nCLEANING VALIDATION")

#Check number of rows
print("Rows:", len(clean_df))

#Check number of columns
print("Columns:",len(clean_df.columns))

#check missing values
print("\nMissing Values:")
print(clean_df.isnull().sum())

#Check duplicate rows
print("\nDuplicate Rows:")
print(clean_df.duplicated().sum())

#Check Shift values
print("\nShift Categories:")
print(clean_df["Shift"].unique())

#Check target distibution
print("\nComplied Distribution:")
print(clean_df["Complied"].value_counts())

# 7. Investigate Duplicate Opportunity IDs
print("\nDUPLICATE OPPORTUNITY INVESTIGATION")


duplicate_ids=clean_df[
    clean_df["Opp"].duplicated(keep=False)
]


print(duplicate_ids.to_string(index=False))

print("\nNumber of duplicated records:")
print(len(duplicate_ids))

print("\nUnique duplicated IDs:")
print(duplicate_ids["Opp"].unique())


#8. Missing Values Analysis
print("\nMISSING VALUES ANALYSIS")

missing_count = clean_df.isnull().sum()

missing_percentage = (missing_count / len(clean_df)) * 100

missing_summary = pd.DataFrame({
    "Missing Count": missing_count,
    "Missing Percentage": missing_percentage
})

print(missing_summary)


# 9. Investigate Missing Values Patterns

print("\nHHaction Missing Values vs Complied")

clean_df["HHaction_Missing"] = clean_df["HHaction"].isnull()

print(pd.crosstab(
    clean_df["HHaction_Missing"],
    clean_df["Complied"]
))

print("\nMissedbutglove Missing Values vs Complied")

clean_df["Missedbutglove_Missing"] = clean_df["Missedbutglove"].isnull()

print(pd.crosstab(
    clean_df["Missedbutglove_Missing"],
    clean_df["Complied"]
))


