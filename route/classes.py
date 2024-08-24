from typing import List
from model.classes import classes
from fastapi import APIRouter, Response
from ai.langchain import response
from config.db import engine, meta_data
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from schema.class_schema import ClassSchemaInput, ClassSchemaOutput

class_route = APIRouter()


@class_route.get("/classes", response_model=List[ClassSchemaOutput], status_code=HTTP_200_OK)
def list_classes():
    with engine.connect() as conn:
        result = conn.execute(classes.select()).fetchall()
        return result


@class_route.get('/classes/{id}')
def get_class(id: str):
    with engine.connect() as conn:
        result = conn.execute(classes.select().where(classes.c.id == id)).first()
        return result

@class_route.post('/classes', status_code=HTTP_201_CREATED )
def store_class(data_class: ClassSchemaInput):
    with engine.connect() as conn:
        new_class = data_class.dict()
        result = conn.execute(classes.insert().values(new_class))
        conn.commit()
        return "Success"



@class_route.put('/classes/{id}', response_model=ClassSchemaInput, status_code=HTTP_201_CREATED)
def update_class(data_class: ClassSchemaInput, id: str):
    with engine.connect() as conn:
        conn.execute(classes.update().values(
            name=data_class.name,
            description=data_class.description,
            prompt_question= data_class.prompt_question,
            prompt_response= data_class.prompt_response,
        ).where(classes.c.id == id))
        conn.commit()
        result = conn.execute(classes.select().where(classes.c.id == id)).first()
        return result



@class_route.delete('/classes/{id}')
def delete_class(id: str):
    with engine.connect() as conn:
        conn.execute(classes.delete().where(classes.c.id == id))
        return Response(status_code=HTTP_204_NO_CONTENT)


