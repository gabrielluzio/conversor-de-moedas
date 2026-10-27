import re
from pydantic import BaseModel, Field, field_validator
from typing import List

class validar_moeda(BaseModel):
    preco: float = Field(gt=0)
    moeda_destino: list[str]

    @field_validator("moeda_destino")
    @classmethod
    def validar(cls, value):
        for moedas in value:
            if not re.fullmatch('^[A-Z]{3}$', moedas):
                raise ValueError(f'moeda invalida {moedas}')
        return value