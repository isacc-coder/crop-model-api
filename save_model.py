# save_model.py
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Generate synthetic dataset
np.random.seed(42)
num_samples = 200

data = pd.DataFrame({
    'nitrogen': np.random.uniform(0, 100, num_samples),
    'phosphorus': np.random.uniform(0, 100, num_samples),
    'potassium': np.random.uniform(0, 100, num_samples),
    'temperature': np.random.uniform(10, 40, num_samples),
    'humidity': np.random.uniform(30, 90, num_samples),
    'ph': np.random.uniform(4, 9, num_samples),
    'rainfall': np.random.uniform(20, 300, num_samples),
})

# Simulate crop labels
labels = np.random.choice(['wheat', 'maize', 'rice', 'barley', 'sorghum'], num_samples)

# Train model
X = data
y = labels
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model/crop_model.pkl")

print("✅ Demo seed recommendation model saved as 'model/crop_model.pkl'")
