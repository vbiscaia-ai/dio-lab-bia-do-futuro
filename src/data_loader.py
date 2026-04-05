import pandas as pd
import streamlit as st
from config import Config

class DataLoader:
    @staticmethod
    @st.cache_data
    def carregar_kpis():
        try:
            expediente = pd.read_csv(f"{Config.CAMINHO_DADOS}KPI/estornos_pos_expediente.csv")
            lojas = pd.read_csv(f"{Config.CAMINHO_DADOS}Total de fraudes por loja.csv")
            return expediente, lojas
        except Exception as e:
            return None, None