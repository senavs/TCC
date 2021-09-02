from pydantic import BaseModel


class PredictRequest(BaseModel):
    file: str


class PredictResponse(BaseModel):
    prediction: str


class PredictFormResponse(BaseModel):
    prediction: str
