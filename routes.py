from asyncio import gather
from fastapi import APIRouter, Query
import re
from converter import async_converter_moeda
from schemas import validar_moeda 

Router = APIRouter(prefix = "/converter", tags = ["/converter'"])


@Router.post("/converter")
async def converter(
            body: validar_moeda,
            moeda_origem: str = Query(max_length=3, pattern= '^[A-Z]{3}$'),              
            ):

    moeda_destino = body.moeda_destino
    preco = body.preco

    lista_moeda_convertida = []

    for moeda in moeda_destino:
        result = async_converter_moeda(
            moeda_origem=moeda_origem,
            moeda_destino=moeda,
            preco=preco
            )

        lista_moeda_convertida.append(result)

    resultado_corrotina = await gather(*lista_moeda_convertida)    
    return resultado_corrotina