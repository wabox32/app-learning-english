from fastapi import FastAPI
from route.classes import classes
from route.levels import levels

app = FastAPI()
app.include_router(classes)
app.include_router(levels)

