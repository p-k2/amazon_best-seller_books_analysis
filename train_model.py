# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle
import numpy as np

# Load dataset
df = pd.read_csv("data/bestseller.csv")
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# Features and target
X = df[["Price", "Publication Year", "Genre"]]
y = df["Rating"]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("genre", OneHotEncoder(handle_unknown="ignore"), ["Genre"])
    ],
    remainder="passthrough"  # keep price + year
)

# Model pipeline
model = Pipeline(steps=[
    ("preprocess", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=200, random_state=42))
])

# Train-test split (optional—but good practice)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)
# Predict on test data
y_pred = model.predict(X_test)
# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n📊 MODEL PERFORMANCE")
print(f"MAE  : {mae:.3f}")
print(f"MSE  : {mse:.3f}")
print(f"RMSE : {rmse:.3f}")
print(f"R² Score : {r2:.3f}")
# Save model
pickle.dump(model, open("models/rating_model.pkl", "wb"))

print("✔ Model trained and saved as rating_model.pkl")
