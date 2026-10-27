from fastapi import FastAPI
from routes import Router

app = FastAPI(
    tittle = "API de conversor de moedas",
    description = "API REST para conversor de moedas",
    version="1.0.0"
)


app.include_router(Router)