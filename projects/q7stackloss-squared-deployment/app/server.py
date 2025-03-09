# API Server for the model

from fastapi import FastAPI
import joblib
from typing import List
import numpy as np


model = joblib.load('./q7stackloss-quadratic-model.joblib')
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "You are accessing the q7stackloss-quadratic-model!"}

@app.get("/predict")
async def predict(x: str):
    # Convert comma-separated string to list of numbers. e.g. 62, 22, 87, 484, 7569
    x_list = [float(i) for i in x.split(',')]
    X = np.array(x_list).reshape(1, -1)
    prediction = model.predict(X)
    return {"prediction": prediction[0]}

# create post for sample input data {"X": [80, 27, 89, 42, 95]}
@app.post("/predict")
async def predict(data: dict):
    # Convert input to numpy array
    X = np.array(data['X']).reshape(1, -1)

    # Make prediction
    prediction = model.predict(X)

    # Return prediction as JSON
    return {"Prediction": prediction[0]}




