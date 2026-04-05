# 📂 Exemplos e Referências

Esta pasta contém guias práticos e referências de implementação para cada etapa do desenvolvimento do **FraudGuard AI**.

## 🎬 Vídeos de Referência

> [!IMPORTANT]
> Os vídeos abaixo demonstram o raciocínio analítico aplicado para transformar os **102.000 registros** em uma IA de decisão.

| Etapa | Descrição | Status |
|:---|:---|:---|
| **Documentação** | Definição do pipeline de dados e arquitetura RAG. | [Em breve] |
| **Base de Conhecimento** | Estruturação dos KPIs em `/data/KPI/` (Teto de R$ 934,00). | [Em breve] |
| **Prompts** | Engenharia de Prompt para o "Analista Sênior de Risco". | [Em breve] |
| **Aplicação** | Demonstração da interface **Streamlit** em tempo real. | [Em breve] |
| **Métricas** | Como validamos a assertividade contra fraudes históricas. | [Em breve] |
| **Pitch** | Apresentação executiva da solução para o ecossistema Bradesco. | [Em breve] |

## 🚀 Exemplo de Implementação Simples

Confira na pasta `src/` o arquivo `app.py`. Ele contém a estrutura base da aplicação, utilizando:
* **Streamlit:** Para a interface de usuário.
* **Pandas:** Para a leitura rápida dos CSVs de métricas.
* **Integração LLM:** Onde o prompt de sistema é injetado para analisar o risco.

---
> [!TIP]
> Caso queira replicar a lógica de análise para outros dados (como os alarmes industriais), basta ajustar o caminho do arquivo na base de conhecimento dentro do código fonte.
