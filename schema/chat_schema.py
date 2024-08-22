from pydantic import BaseModel
from typing import Optional

class ChatSchemaInput(BaseModel):
    question: str


class ChatSchemaOutput(BaseModel):
    id: Optional[int]
    question: str
    response: str