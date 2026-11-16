BIOPRESS – DATA ENGINEERING README

1. PROJECT DATASET
Main dataset:
data/modeling_dataset.csv

Total Records: 917
Total Columns: 5
Missing Values: 0

2. APPROVED FEATURES
Input Features:
- Ward
- Profcat
- Shift
- Indication

Target:
- Complied (Yes / No)

3. DATA PREPARATION
- Inspected the original dataset.
- Standardized Shift values.
- Analyzed missing values.
- Excluded leakage-related columns.
- Created the modeling dataset.
- Configured OneHotEncoder preprocessing.
- Validated preprocessing using a train/test split.
- Performed final data validation.

4. IMPORTANT NOTES FOR AI TEAM
- Do not use Opp as a predictive feature.
- Do not use HHaction or Missedbutglove as predictors.
- Fit preprocessing only on training data.
- Consider class imbalance.
- Investigate repeated feature combinations.
- Independence of observations has not been confirmed.
- Avoid interpreting model performance as causal evidence.

5. DATASET LIMITATIONS
- The dataset contains 917 observations.
- Target classes are imbalanced:
  No: 715
  Yes: 202
- The meaning and uniqueness of Opp have not been confirmed.

6. CURRENT STATUS
Data inspection: Completed
Data cleaning: Completed
Feature selection: Completed
Preprocessing configuration: Completed
Data validation: Passed
Documentation: Prepared

Model training and evaluation:
Handled by the AI team.
