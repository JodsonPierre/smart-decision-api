import streamlit as st # type: ignore
import requests # type: ignore

# Título do site
st.title("🏠 Comprar ou Alugar? SmartDecision")

# Campos para o usuário digitar
valor_casa = st.number_input("Qual o valor do imóvel? (R$)", value=300000)
aluguel = st.number_input("Qual o valor do aluguel mensal? (R$)", value=1500)
selic = st.number_input("Qual a taxa Selic atual? (%)", value=10.5)

if st.button("Calcular Melhor Opção"):
    # Aqui o garçom leva o pedido para a cozinha (o seu back-end)
    # Por enquanto, usamos o endereço do seu computador
    url = f"http://127.0.0.1:8888/comparar?valor_casa={valor_casa}&aluguel={aluguel}&selic={selic}"
    
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        st.success(f"**Decisão:** {dados['decisao']}")
        st.info(f"**Motivo:** {dados['motivo']}")
    else:
        st.error("Erro ao falar com o motor da calculadora!")