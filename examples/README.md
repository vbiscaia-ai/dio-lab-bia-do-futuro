# 📂 Exemplos e Referências

Esta pasta contém guias práticos e referências de implementação para cada etapa do desenvolvimento do **FraudGuard AI**.

## 🎬 Vídeos de Referência e Raciocínio Analítico

> [!IMPORTANT]
> Os vídeos abaixo demonstram o raciocínio aplicado para transformar **102.000 registros** brutos em uma IA de decisão estratégica.

| Etapa | Descrição | Status |
|:---|:---|:---|
| **Documentação** | Definição do pipeline de dados e arquitetura RAG (Retrieval-Augmented Generation). | ⏳ [Em breve] |
| **Base de Conhecimento** | Estruturação dos KPIs em `/data/KPI/` (Ex: Teto de R$ 934,00). | ⏳ [Em breve] |
| **Prompts** | Engenharia de Prompt focada no papel de "Analista Sênior de Risco". | ✅ [Disponível] |
| **Aplicação** | Demonstração da interface **Streamlit** em tempo real. | ✅ [Disponível] |
| **Métricas** | Metodologia de validação contra bases de fraudes históricas. | ⏳ [Em breve] |
| **Pitch** | Apresentação executiva da solução para o ecossistema Bradesco/DIO. | ✅ [Disponível] |

## 🚀 Exemplo de Implementação Simples

Para entender a base técnica, explore o arquivo `src/engine.py`. A solução foi construída sobre três pilares:

1.  **Streamlit:** Camada de interface para entrada de dados transacionais.
2.  **Pandas:** Motor para processamento e filtragem das métricas de segurança (CSVs).
3.  **LLM Reasoning:** Injeção de prompts de sistema que orientam a IA a decidir com base em horários e valores críticos.

---

> [!TIP]
> **Versatilidade da Lógica:** > Esta mesma arquitetura de "Motor de Decisão" pode ser adaptada para outros domínios. Por exemplo, ao ajustar a base de conhecimento para **KPIs industriais (MTTR/MTBF)**, o agente passaria a identificar criticidade em ativos industriais com base em alarmes e tempo de parada, em vez de transações financeiras.

---
**Analista Responsável:** Victor Biscaia  
**Foco:** Engenharia de Dados & Business Intelligence
