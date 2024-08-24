from fastapi import FastAPI
from route.classes import class_route
from route.levels import levels
from route.chats import chats
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
app.include_router(class_route)
app.include_router(levels)
app.include_router(chats)

