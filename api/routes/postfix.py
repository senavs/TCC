from fastapi import APIRouter

from api.models.postfix import ConvertRequest, ConvertResponse, EvaluateRequest, EvaluateResponse
from api.modules.postfix import to_postfix, crete_space_between_symbols, evaluate

router = APIRouter(prefix='/postfix', tags=['Calculus'])


@router.post('/convert', status_code=200, response_model=ConvertResponse)
def _convert(body: ConvertRequest) -> ConvertResponse:
    postfix = to_postfix(crete_space_between_symbols(body.infix))
    return ConvertResponse(postfix=postfix)


@router.post('/evaluate', status_code=200, response_model=EvaluateResponse)
def _evaluate(body: EvaluateRequest) -> EvaluateResponse:
    result = evaluate(body.postfix)
    return EvaluateResponse(result=result)
