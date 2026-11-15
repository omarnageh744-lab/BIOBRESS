import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.pipeline import Pipeline

# 1. Load modeling dataset
df = pd.read_csv("data/modeling_dataset.csv")
print("\nORIGINAL INDICATION VALUES")
print(df["Indication"].unique())

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

# 4. Create OneHotEncoder
preprocessor = ColumnTransformer(
    transformers=[
        ("categorical", OneHotEncoder(handle_unknown="ignore"),
         categorical_features)
    ]
)

# 5. Encode Target
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# 6. Create Pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor)
    ]
)

# 7. Transform Features
X_encoded = pipeline.fit_transform(X)

# 8. Validation
print("\nENCODING VALIDATION")

print("Original Features Shape:", X.shape)
print("Encoded Features Shape:", X_encoded.shape)

print("\nTarget Classes:")
print(label_encoder.classes_)

print("\nEncoded Target Distribution:")
print(pd.Series(y_encoded).value_counts())

print("\nFeature Names:")
print(pipeline.named_steps["preprocessor"].get_feature_names_out())

print("\nEncoding completed successfully!")