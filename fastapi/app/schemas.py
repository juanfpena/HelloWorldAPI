from pydantic import BaseModel


class Calculator(BaseModel):
    a: int
    b: int
    operation: str
