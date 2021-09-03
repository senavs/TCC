from typing import Optional

from pydantic import BaseModel


class PredictRequest(BaseModel):
    file: str


class PredictImageResponse(BaseModel):
    prediction: str


class PredictExpressionResponse(BaseModel):
    symbols: list[str]
    expression: str
    postfix: Optional[str] = None
    result: Optional[int] = None
    error: Optional[str] = None
