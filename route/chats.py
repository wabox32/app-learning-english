from fastapi import APIRouter
from schema.chat_schema import ChatSchemaInput
from ai.langchain import response
from config.db import engine, meta_data
from model.chat import chat
from model.classes import classes
from schema.chat_schema import ChatSchemaOutput
from typing import List

chats = APIRouter()

@chats.post('/chats/{id}')
def get_response(data_chat: ChatSchemaInput, id: str):
    with engine.connect() as conn:
        result = conn.execute(classes.select().where(classes.c.id == id)).first()
        data = data_chat.dict()
        return response(result.prompt_question, data_chat.question)


@chats.get('/chats/{id}', response_model=List[ChatSchemaOutput])
def get_chat(id: str):
    with engine.connect() as conn:
        result = conn.execute(chat.select()).feachAll().limit(10)
        return result