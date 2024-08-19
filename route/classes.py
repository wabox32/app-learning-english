from fastapi import APIRouter

classes = APIRouter()


@classes.get("/")
def getClasses():
    return "listado de clases"