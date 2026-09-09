from contextlib import asynccontextmanager
# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from database import create_tables
import model

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Application Starting")
    create_tables()
    print("DB Tables created")
    yield
    print("Application shutting down")

app = FastAPI(
    title="Rangmanch Reviews API",
    description="Theatre reviews API for Pune Rangmanch",
    lifespan=lifespan
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Rangmanch Reviews API"}
