import streamlit as st
from engine import FraudEngine
from data_loader import DataLoader

st.set_page_config(page_title="FraudGuard AI", page_icon="🛡️")

# --- AJUSTE AQUI ---
# Isso garante que o motor da IA só ligue uma vez, poupando sua cota!
@st.cache_resource
def get_engine():
    return FraudEngine()

engine = get_engine()
# -------------------

df_exp, df_lojas = DataLoader.carregar_kpis()

st.title("🛡️ FraudGuard AI - Dashboard de Risco")

# Inputs
with st.sidebar:
    st.header("Simulação")
    valor = st.number_input("Valor", value=100.0)
    loja = st.text_input("Loja", "Loja 1")
    horario = st.text_input("Horário (HH:MM)", "14:00")
    btn = st.button("Analisar")

if btn:
    with st.spinner("Analisando risco com IA..."): # Adiciona um feedback visual
        resultado = engine.analisar(valor, loja, horario)
        st.subheader("Resultado da Análise")
        st.info(resultado)