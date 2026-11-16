import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

# 1. Load modeling dataset
df = pd.read_csv("data/modeling_dataset.csv")

# 2. Separate Features and Target
X = df[["Ward", "Profcat", "Shift", "Indication"]]
y = df["Complied"]

# 3. Define categorical features
categorical_features = [
    "Ward",
    "Profcat",
    "Shift",
    "Indication"
]

# 4. Create preprocessing transformer
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)

# 5. Create preprocessing pipeline
preprocessing_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor)
    ]
)

# 6. Validate pipeline configuration
print("\nPREPROCESSING PIPELINE VALIDATION")

print("Dataset Shape:", df.shape)

print("Features:", X.columns.tolist())

print("Target:", y.name)

print("Pipeline Steps:")
print(preprocessing_pipeline.named_steps.keys())

print("\nPreprocessing Pipeline Created Successfully!")
