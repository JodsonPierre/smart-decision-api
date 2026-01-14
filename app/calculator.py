# app/calculator.py

def comparar_investimento(valor_imovel, valor_aluguel, taxa_selic):
    # Se eu tenho o dinheiro do imóvel e invisto na Selic
    rendimento_mensal = (valor_imovel * (taxa_selic / 100)) / 12
    
    if rendimento_mensal > valor_aluguel:
        return {
            "decisao": "Alugar e Investir",
            "motivo": f"Seu dinheiro rende R${rendimento_mensal:.2f}, que paga o aluguel e sobra!"
        }
    else:
        return {
            "decisao": "Comprar o Imóvel",
            "motivo": "O aluguel está mais caro que o rendimento do dinheiro parado."
        }