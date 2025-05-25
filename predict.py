# predict.py
import joblib
import numpy as np
import os



model_path = os.path.join(os.path.dirname(__file__), "model", "crop_model.pkl")
model = joblib.load(model_path)

def predict_crop(data):
    input_data = np.array([
        data.nitrogen,
        data.phosphorus,
        data.potassium,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction[0]
