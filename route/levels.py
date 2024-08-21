from fastapi import APIRouter, Response
from config.db import engine, meta_data
from model.level import level
from schema.level_schema import LevelSchemaInput, LevelSchemaOutput
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT

levels = APIRouter()

@levels.get("/levels", response_model=List[LevelSchemaOutput], status_code=HTTP_200_OK)
def list_level():
    with engine.connect() as conn:
        result = conn.execute(level.select()).fetchall()
        return result
    
@levels.post("/levels", status_code=HTTP_201_CREATED )
def create_level(data_level: LevelSchemaInput):
    with engine.connect() as conn:
        new_level = data_level.dict()
        result = conn.execute(level.insert().values(new_level))
        conn.commit()
        return "Success"

@levels.put("/levels/{id}", response_model=LevelSchemaInput, status_code=HTTP_201_CREATED)
def update_level(data_level: LevelSchemaInput, id: str):
    with engine.connect() as conn:
        conn.execute(level.update().values(
            name=data_level.name,
            description=data_level.description
        ).where(level.c.id == id))
        conn.commit()
        result = conn.execute(level.select().where(level.c.id == id)).first()
        return result

@levels.get("/levels/{id}", response_model=LevelSchemaOutput, status_code=HTTP_200_OK)
def get_level(id:str):
    with engine.connect() as conn:
        result = conn.execute(level.select().where(level.c.id == id)).first()
        return result

@levels.delete("/levels/{id}", status_code=HTTP_204_NO_CONTENT)
def delete_level(id:str):
    with engine.connect() as conn:
        conn.execute(level.delete().where(level.c.id == id))
        return Response(status_code=HTTP_204_NO_CONTENT)