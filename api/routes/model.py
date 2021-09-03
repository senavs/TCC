from fastapi import APIRouter, File

from api.models.model import PredictRequest, PredictImageResponse, PredictExpressionResponse
from api.modules.model import load_model, predict
from api.modules.postfix import create_expression, to_postfix, evaluate
from api.modules.preprocessing import bytes_to_numpy, base64_to_numpy, get_image_bounding_box, padding

router = APIRouter(prefix='/model', tags=['Model'])

model = load_model()


@router.post('/image/predict', status_code=200, response_model=PredictImageResponse)
def _predict_image(body: PredictRequest) -> PredictImageResponse:
    image = base64_to_numpy(body.file)
    prediction = predict(model, image)
    return PredictImageResponse(prediction=prediction)


@router.post('/image/form/predict', status_code=200, response_model=PredictImageResponse)
def _predict_image_form(file_bytes: bytes = File(...)) -> PredictImageResponse:
    image = bytes_to_numpy(file_bytes)
    prediction = predict(model, image)
    return PredictImageResponse(prediction=prediction)


@router.post('/expression/form/predict', status_code=200, response_model=PredictExpressionResponse)
def _predict_expression_form(file_bytes: bytes = File(...)) -> PredictExpressionResponse:
    image = bytes_to_numpy(file_bytes)

    symbols = []
    for roi in get_image_bounding_box(image):
        padded_image = padding(roi)
        symbols.append(predict(model, padded_image))

    expression = create_expression(*symbols)
    error = None
    try:
        postfix = to_postfix(expression)
        result = evaluate(postfix)
    except Exception as err:
        postfix = None
        result = None
        error = str(err)
    return PredictExpressionResponse(symbols=symbols, expression=expression, postfix=postfix, result=result, error=error)
