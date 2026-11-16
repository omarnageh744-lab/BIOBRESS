import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.base import clone
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

# 1. Load dataset
df = pd.read_csv("data/modeling_dataset.csv")

# 2. Separate Features and Target
X = df[["Ward", "Profcat", "Shift", "Indication"]]
y = df["Complied"]

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# 4. Create preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            ["Ward", "Profcat", "Shift", "Indication"]
        )
    ]
)

# 5. Create pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor)
    ]
)

# 6. Fit only on training data
X_train_encoded = pipeline.fit_transform(X_train)

# 7. Transform test data
X_test_encoded = pipeline.transform(X_test)

# 8. Validation
print("\nPREPROCESSING VALIDATION")

print("Training Records:", len(X_train))
print("Testing Records:", len(X_test))

print("Training Encoded Shape:", X_train_encoded.shape)
print("Testing Encoded Shape:", X_test_encoded.shape)

print("\nTraining Target Distribution:")
print(y_train.value_counts())

print("\nTesting Target Distribution:")
print(y_test.value_counts())

print("\nSame Number of Features:",
      X_train_encoded.shape[1] == X_test_encoded.shape[1])

print("\nPreprocessing Validation Completed!")