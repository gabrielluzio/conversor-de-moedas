# Conversor de Moedas API

API REST desenvolvida em **Python com FastAPI** para realizar conversões de moedas utilizando taxas de câmbio consultadas através da API Alpha Vantage.

O projeto foi desenvolvido com o objetivo de praticar o desenvolvimento de APIs, integração com serviços externos, validação de dados e tratamento de erros.

## Tecnologias utilizadas

- Python
- FastAPI
- Pydantic
- Requests HTTP
- Alpha Vantage API
- Swagger UI

## Funcionalidades

- Conversão de valores entre diferentes moedas.
- Consulta de taxas de câmbio através de uma API externa.
- Validação dos dados enviados pelo usuário.
- Tratamento de erros durante as requisições.
- Documentação automática dos endpoints com Swagger UI.

## Como funciona

O usuário informa a moeda de origem, a moeda de destino e o valor que deseja converter.

A aplicação consulta a taxa de câmbio na API Alpha Vantage, realiza o cálculo e retorna o resultado da conversão.

## Endpoint

**POST `/converter`**

Responsável por receber os dados da conversão e retornar o valor convertido.

## Como executar

1. Clone este repositório.
2. Instale as dependências do projeto.
3. Configure sua chave da API Alpha Vantage no ambiente.
4. Inicie a aplicação FastAPI.
5. Acesse `http://127.0.0.1:8000/docs` para testar a API pelo Swagger.

## Aprendizados

Durante o desenvolvimento deste projeto, pratiquei:

- Criação de endpoints com FastAPI.
- Integração com APIs externas.
- Manipulação de respostas JSON.
- Validação de dados com Pydantic.
- Tratamento de exceções e erros HTTP.
- Organização de um projeto backend em Python.

## Sobre o projeto

Este projeto faz parte dos meus estudos em desenvolvimento backend com Python e da construção do meu portfólio no GitHub.
