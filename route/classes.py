from typing import List
from model.classes import classes
from fastapi import APIRouter, Response
from ai.langchain import response
from config.db import engine, meta_data
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from schema.class_schema import ClassSchemaInput, ClassSchemaOutput

classes = APIRouter()


@classes.get("/classes", response_model=List[ClassSchemaOutput], status_code=HTTP_200_OK)
def list_classes():
    with engine.connect() as conn:
        result = conn.execute(classes.select()).feachAll()
        return result
        """ res = response("Eres un profesor de ingles tu mision es enseñar sobre el presente simple le haras preguntas al estaduiante y tu le informaras que errores tiene y como debio ser la respuesta", "estoy listo")
        return res"""


@classes.get('/classes/{id}')
def get_class(id: str):
    with engine.connect() as conn:
        result = conn.execute(classes.select().where(classes.c.id == id)).first()
        return result

@classes.post('/classes', status_code=HTTP_201_CREATED )
def store_class(data_class: ClassSchemaInput):
    with engine.connect() as conn:
        new_class = data_class.dict()
        result = conn.execute(classes.insert().values(new_class))
        conn.commit()
        return "Success"



@classes.put('/classes/{id}', response_model=ClassSchemaInput, status_code=HTTP_201_CREATED)
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



@classes.delete('/classes/{id}')
def delete_class(id: str):
    with engine.connect() as conn:
        conn.execute(classes.delete().where(classes.c.id == id))
        return Response(status_code=HTTP_204_NO_CONTENT)


