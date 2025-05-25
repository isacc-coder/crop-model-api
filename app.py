# # app.py
# from fastapi import FastAPI
# from pydantic import BaseModel
# from predict import predict_crop

# app = FastAPI()

# class CropInput(BaseModel):
#     nitrogen: float
#     phosphorus: float
#     potassium: float
#     temperature: float
#     humidity: float
#     ph: float
#     rainfall: float

# @app.post("/predict")
# def get_crop_recommendation(input: CropInput):
#     crop = predict_crop(input)
#     return {"recommended_crop": crop}


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    temperature: float
    humidity: float
    rainfall: float

@app.post("/predict")
def predict_crop(data: InputData):
    # Your prediction logic here
    return {"recommended_crop": "wheat"}
