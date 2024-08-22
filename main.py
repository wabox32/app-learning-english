from fastapi import FastAPI
from route.classes import classes
from route.levels import levels
from route.chats import chats

app = FastAPI()
app.include_router(classes)
app.include_router(levels)
app.include_router(chats)

