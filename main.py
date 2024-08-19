from fastapi import FastAPI
from route.classes import classes


app = FastAPI()
app.include_router(classes)

