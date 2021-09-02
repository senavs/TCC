from fastapi import APIRouter, File

from api.models.model import PredictFormResponse, PredictRequest, PredictResponse
from api.modules.model import load_model, predict
from api.modules.preprocessing import bytes_to_numpy, base64_to_numpy

router = APIRouter(prefix='/model', tags=['Model'])

model = load_model()


@router.post('/image/predict', status_code=200, response_model=PredictResponse)
def _predict_image(body: PredictRequest) -> PredictResponse:
    image = base64_to_numpy(body.file)
    prediction = predict(model, image)
    return PredictResponse(prediction=prediction)


@router.post('/image/form/predict', status_code=200, response_model=PredictFormResponse)
def _predict_form(file_bytes: bytes = File(...)) -> PredictFormResponse:
    image = bytes_to_numpy(file_bytes)
    prediction = predict(model, image)
    return PredictFormResponse(prediction=prediction)
