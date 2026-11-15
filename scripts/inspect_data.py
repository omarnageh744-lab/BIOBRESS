import pandas as pd  
import os 

#====================================
#1. Load Dataset
#====================================
file_path="data/hand_hygiene_data_labeled.csv"

df=pd.read_csv(file_path)
print("=" *50)
print("BIOPRESS - DATASET INSPECTION")
print("=" * 50)
#======================================
#2. Dataset Information
#===================================== 
print("\n1. DATASET SHAPE")
print("Rows:",df.shape[0])
print("Columns:", df.shape[1])

print("\n2. COLUMN NAMES")
print(df.columns.tolist())
#=====================================
#3.Data Types
#=====================================
print("\n3. DATA TYPES")
print(df.dtypes)

#====================================
#4. Missing Values
#====================================
print("\n4. MISSING VALUES")
missing=df.isnull().sum()
print(missing)
print("\nMissing Percentage:")
missing_percentage=(missing/len(df))*100
print(missing_percentage.round(2))

#====================================
#5.Duplicate Rows
#====================================
print("\n5. DUPLICATE ROWS")
duplicates=df.duplicated().sum()
print("Duplicate Rows:",(duplicates))

#===================================
#6. Unique Values
#===================================
print("\n6. UNIQUE VALUES")
for column in df.columns:
    print("\nColumn:", column)
    print(df[column].value_counts(dropna=False))
#==================================
#7. Target label Analyses
#==================================
print("n\7. TARGET LABEL ANALYSES")
target="Complied"
print(df[target].value_counts())
print("\nTarget Percentage:")
print(df[target].value_counts(normalize=True).mul(100).round(2))
#=================================
#8.Duplicate Opportunity IDs
#=================================
print("\n8. DUPLICATE OPPORTUNITY IDs")
print("Duplicate Opp:",df["Opp"].duplicated().sum())
print(df[df["Opp"].duplicated(keep=False)].sort_values("Opp"))

#=================================
#9.Save Initial Report 
#================================
os.makedirs("reports",exist_ok=True)
with open("reports/week1_inspection.txt","w",encoding="utf-8")as f:
    f.write("BIOPRESS DATA QUALITY REPORT\n")
    f.write("="*40+"\n")
    
    f.write(f"\nRows:{df.shape[0]}\n")
    f.write(f"Columns: {df.shape[1]}\n") 
    
    f.write("\ncolumn Names:\n")
    f.write(str(df.columns.tolist()))
    
    f.write("\n\nData Types:\n")
    f.write(df.dtypes.to_string())
    
    f.write("\n\nMissing Values:\n")
    f.write(missing.to_string())
    
    f.write("\n\nMissing Percentage:\n")
    f.write(missing_percentage.round(2).to_string())
    
    f.write(f"\n\nDuplicate Rows:{duplicates}\n") 
    
    f.write("\n\nTarget Distribution:\n")
    f.write(df[target].value_counts().to_string())
    
    f.write("\n\nDuplicate Oppotunity IDs:\n")
    f.write(df[df["Opp"].duplicated(keep=False)].sort_values("Opp").to_string())
    
print("\nReport saved successfly!")
#=================================
#10.Validate Categories
#=================================
print("\n10.CATEGORY VALIDATION")
allowed_values={
    "Ward":[
        "Medical","NICU","Ob/Gyn",
        "Paediatric","Surgical"
    ],
    "Profcat":[
        "Medical doctor", "Midwife",
        "Nurse","Other"
    ],
    "Shift":[
        "Morning","Afternoon","After noon","Night"
    ],
    "Complied":["Yes","No"]
}
for column, allowed in allowed_values.items():
    invalid=df[
        ~df[column].isin(allowed)
    ][column].unique()
    
    print("\nColumn:", column)
    print("Invaled Values:", invalid)

#==================================
#11. check Empty Strings
#==================================
print("\n11. EMPTY STRINGS")
for column in df.columns:
    empty_count=(
        df[column]
        .astype("string")
        .str.strip()
        .eq("")
        .sum()
        )
    print(column," : ",empty_count)
    
#=================================
#12. check Numeric Range
#=================================
print("\n12.OPPORTUNITY ID RANGE")
print("Minimum:",df["Opp"].min())
print("Maximum:",df["Opp"].max())
print("Unique IDs:",df["Opp"].nunique()) 
#================================
#13. INDICATION VALIDATION
#================================
allowed_indications=[
    "Before patient contact",
    "Before an aseptic procedure",
    "After patient contact",
    "After contact with patient Surroundings",
    "After body fluid exposure"
    ]
invalid_indications=df.loc[
    ~df["Indication"].isin(allowed_indications),
    "Indication"
].unique()
print("\n13. INDICATION VALIDATION")
print("Invalid Values:", invalid_indications)