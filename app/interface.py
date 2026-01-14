import streamlit as st
from calculator import comparar_investimento

# Título que aparece no site
st.set_page_config(page_title="SmartDecision", page_icon="🏠")
st.title("🏠 Comprar ou Alugar? SmartDecision")
st.subheader("O seu motor de decisões financeiras")

# Explicação simples para o usuário
st.write("Preencha os dados abaixo e nosso motor de back-end dirá a melhor opção para o seu bolso!")

# Campos para o usuário digitar (Entradas)
valor_casa = st.number_input("Qual o valor do imóvel? (R$)", value=300000, step=1000)
aluguel = st.number_input("Qual o valor do aluguel mensal? (R$)", value=1500, step=100)
selic = st.number_input("Qual a taxa Selic atual? (%)", value=10.5, step=0.1)

# O botão que faz a mágica acontecer
if st.button("Calcular Melhor Opção"):
    # Aqui o Front chama o Back (a função que você criou no calculator.py)
    with st.spinner('O motor está calculando...'):
        resultado = comparar_investimento(valor_casa, aluguel, selic)
    
    # Mostra o resultado bonitão na tela
    st.divider()
    st.header(f"Resultado: {resultado['decisao']}")
    st.info(f"💡 **Por que?** {resultado['motivo']}")
    
# Rodapé do seu portfólio
st.caption("Projeto desenvolvido para portfólio de Back-end Python.")
