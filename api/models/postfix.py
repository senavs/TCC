from pydantic import BaseModel


class ConvertRequest(BaseModel):
    infix: str


class ConvertResponse(BaseModel):
    postfix: str


class EvaluateRequest(BaseModel):
    postfix: str


class EvaluateResponse(BaseModel):
    result: int
