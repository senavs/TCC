from fastapi import APIRouter

from api.models.postfix import ConvertRequest, ConvertResponse
from api.modules.postfix import to_postfix, crete_space_between_symbols

router = APIRouter(prefix='/postfix', tags=['Calculus'])


@router.post('/convert', status_code=200, response_model=ConvertResponse)
def _convert(body: ConvertRequest) -> ConvertResponse:
    postfix = to_postfix(crete_space_between_symbols(body.infix))
    return ConvertResponse(postfix=postfix)
