from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

todos = [
    {"id": 1,
     "item": "Read a Book"
     },
    {"id": 2,
     "item": "Eat a Lemon"
     },
    {"id": 3,
     "item": "Surf a wave!"
     },
]

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to todo list"}


@app.get("/todo", tags=["todo"])
async  def get_todos() -> dict:
    return {"data": todos}

@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": { "Todo added." }
    }