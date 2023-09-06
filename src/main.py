from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.chat import chat_routes
from src.users import users_routes

app = FastAPI()

# routes
app.include_router(users_routes.router)
app.include_router(chat_routes.router)

# cors
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
