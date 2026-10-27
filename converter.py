from os import getenv
import aiohttp
import requests
from fastapi import HTTPException

API_CHAVE = getenv("CHAVE_API")

async def async_converter_moeda(moeda_origem: str, moeda_destino: str, preco: float):

    URL_API = (f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={moeda_origem}&to_currency={moeda_destino}&apikey={API_CHAVE}")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=URL_API) as requisicao_API:
                data = await requisicao_API.json()

    except Exception as error:
        raise HTTPException(status_code = 400, detail = str(error))
    
    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code = 400, detail = "Realtime Currency Exchange Rate not in data")

    Taxa_conversão = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    
    return preco * Taxa_conversão

