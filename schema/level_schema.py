from pydantic import BaseModel
from typing import Optional

class LevelSchemaInput(BaseModel):
    name: str
    description: str


class LevelSchemaOutput(BaseModel):
    id: Optional[int]
    name: str
    description: str