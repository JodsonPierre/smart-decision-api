# app/main.py
from fastapi import FastAPI
from calculator import comparar_investimento

app = FastAPI(title="SmartDecision API")

@app.get("/")
def home():
    return {"status": "Motor funcionando!"}

@app.get("/comparar")
def get_comparacao(valor_casa: float, aluguel: float, selic: float):
    resultado = comparar_investimento(valor_casa, aluguel, selic)
    return resultado