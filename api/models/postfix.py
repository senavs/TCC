from pydantic import BaseModel


class ConvertRequest(BaseModel):
    infix: str


class ConvertResponse(BaseModel):
    postfix: str
