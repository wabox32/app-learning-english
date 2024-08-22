from fastapi import APIRouter
from schema.chat_schema import ChatSchemaInput
from ai.langchain import response

chats = APIRouter()

@chats.post('/chats')
def get_response(data_chat: ChatSchemaInput):
    data = data_chat.dict()
    return response("Eres un profesor de ingles me ayudaras aprender ingles me realizaras preguntas con tematica de pasado simpre y yo las contestare luego de que me las contestes me corregiras y me daras otra pregunta diferente el nivel del ingles es A1.", data_chat.question)



