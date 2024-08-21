from pydantic import BaseModel
from typing import Optional

class ClassSchemaInput(BaseModel):
    name: str
    description: str
    prompt_question: str
    prompt_response: str


class ClassSchemaOutput(BaseModel):
    id: Optional[int]
    name: str
    description: str
    prompt_question: str
    prompt_response: str