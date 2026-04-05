# 💻 Código da Aplicação

Esta pasta contém o núcleo lógico e a interface do seu agente de detecção de fraudes.

## 📁 Estrutura do Código

```text
src/
├── app.py             # Interface Streamlit e fluxo de entrada do usuário
├── engine.py          # Lógica do Agente (RAG e integração com LLM)
├── data_loader.py     # Processamento dos KPIs de /data/KPI/
├── config.py          # Variáveis de ambiente e chaves de API
└── requirements.txt   # Dependências do projeto
```

### 📄 Conteúdo do requirements.txt
Para garantir que o ambiente rode perfeitamente, estas são as bibliotecas base:

```
streamlit       # Interface Web
pandas          # Manipulação dos 102k registros (CSV)
python-dotenv   # Gestão de chaves de segurança
google-generativeai # SDK para integração com Gemini
langchain       # Orquestração da base de conhecimento (Opcional)
```

### 🚀 Como Rodar o Projeto Localmente
Siga os passos abaixo para subir o FraudGuard AI na sua máquina:

## 1 Clonar o repositório: 

```
git clone [https://github.com/vbiscaia/dio-lab-fraudguard-ai.git](https://github.com/vbiscaia/dio-lab-fraudguard-ai.git)
cd dio-lab-fraudguard-ai/src
```

## 2 Configurar as Chaves (API Keys):
Crie um arquivo .env na raiz da pasta src/ e adicione sua chave:

```
GEMINI_API_KEY=sua_chave_aqui
```

## 3 Instalar as Dependências:
```
pip install -r requirements.txt
```
## 4 Rodar a Aplicação:

```
# Executar o servidor do Streamlit
streamlit run app.py
```

### [!TIP]
Performance: Como estamos lidando com uma base de dados real, o script data_loader.py utiliza cache do Streamlit (@st.cache_data) para garantir que a leitura dos CSVs de indicadores não impacte a latência da resposta da IA.
