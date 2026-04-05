## 🤖 Agente de Prevenção de Fraudes: Inteligência e Resiliência

# Contexto e Diferenciais

- Este assistente evolui a análise de risco de um sistema baseado em regras estáticas para um agente consultivo de decisão, focado em quatro pilares estratégicos:

- **Antecipação de Riscos:** Identifica padrões de chargeback antes da confirmação da transação, analisando correlações de valor, horário e comportamento.

- **Personalização de Contexto:** Avalia o risco de forma dinâmica, cruzando os dados da transação com a base de conhecimento (RAG) extraída dos meus repositórios de análise de fraude.

- **Decisão Consultiva:** Não apenas bloqueia, mas justifica o score de risco, sugerindo ações imediatas (Revisão Manual ou Aprovação) para o analista de fraude.

- **Confiabilidade e Anti-Alucinação:** Utiliza Engenharia de Prompt e dados estruturados para garantir que cada diagnóstico seja fundamentado em evidências históricas reais.)

## 📺 Demonstração Técnica (Pitch)

Clique na imagem abaixo para assistir à apresentação completa da solução, onde detalho a análise de **517 transações** e a lógica do motor de IA:

[![Assistir ao Pitch FraudGuard AI](https://raw.githubusercontent.com/vbiscaia-ai/dio-lab-bia-do-futuro/main/assets/print_fraudguard.png)](https://www.youtube.com/watch?v=c6e5m0F60J4)

> [!TIP]
> No vídeo, demonstro como identificamos que **100% dos estornos pós-expediente** eram fraudulentos e como a Loja 1 concentrava quase **R$ 2.000,00** em perdas.
---

## 🛡️ Documentação do Agente: FraudGuard AI

### 1. Definição do Agente

O **FraudGuard AI** é um especialista em segurança financeira focado na detecção e prevenção de fraudes em operações de estorno dentro do ecossistema bancário (Bradesco).

- **Caso de Uso:** Identificação de anomalias em solicitações de estorno, mitigando prejuízos operacionais através da análise de padrões históricos (horários críticos, unidades de alto risco e desvios de ticket médio).
- **Persona e Tom de Voz:** Atua como um **Analista de Risco Sênior**. O tom de voz é técnico, preciso e consultivo, baseando cada veredito em evidências estatísticas extraídas da base de dados.
- **Arquitetura:** Utiliza a técnica de **RAG (Retrieval-Augmented Generation)**. O sistema extrai KPIs estratégicos das pastas de dados e os injeta no contexto da LLM para garantir que o score de risco seja fundamentado em dados reais.
- **Segurança:** Para evitar alucinações, o agente utiliza estritamente os limites financeiros (**Teto de R$ 934**) e temporais (**Janela pós-expediente**) definidos nos arquivos consolidados.

 📄 **Template:** [docs/01-documentacao-agente.md](.01-documentacao-agente.md)

---

### 2. Base de Conhecimento (Dados Reais do Projeto)

Substituímos os dados genéricos do bootcamp por uma base de dados personalizada com registros reais de alarmes e transações, organizada da seguinte forma:

| Arquivo / Caminho | Formato | Descrição |
|:--- |:---:|:--- |
| `data/KPI/resumo_geral_transacoes/` | CSV | Base macro com 517 transações e taxa de fraude de **22,44%**. |
| `data/KPI/estornos_pos_expediente/` | CSV | Registros que comprovam **100% de incidência de fraude** após as 18h. |
| `data/KPI/metricas_financeiras_fraude/` | CSV | Parâmetros de Ticket Médio (**R$ 126**) e Teto de Segurança (**R$ 934**). |
| `data/Total de fraudes por loja.csv` | CSV | Ranking de unidades críticas, destacando a **Loja 1** como foco de perdas. |
| `data/deteccao-fraude-estorno.csv` | CSV | Histórico detalhado (46KB) para análise de correlação e comportamento. |
| `data/Horario compras fraudulentas.csv`| CSV | Mapeamento temporal de tentativas de ataque por faixa horária. |


📄 **Template:** [`02-base-conhecimento.md`](./docs/02-base-conhecimento.md)
---


### 🧠 Estratégia de Uso dos Dados no Prompt

A IA não apenas "lê" os arquivos, ela aplica regras de negócio dinâmicas:
1. **Prioridade Crítica:** Se o horário da transação coincide com os dados de `estornos_pos_expediente`, o risco é elevado para 100% automaticamente.
2. **Anomalia de Valor:** Valores que superam o teto de `metricas_financeiras_fraude` disparam um alerta de revisão manual.
3. **Geolocalização de Risco:** Unidades listadas em `Total de fraudes por loja` recebem um incremento no score de criticidade.

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento e as camadas de segurança do seu agente:

#### 🤖 System Prompt

```text
Você é o **FraudGuard AI**, um Especialista Sênior em Prevenção a Fraudes do ecossistema Bradesco. Sua missão é realizar a triagem de solicitações de estorno e fornecer um Score de Risco (%) preciso.

### 🛡️ REGRAS DE OURO (NÃO NEGOCIÁVEIS):
1. **Fidelidade aos Dados:** Baseie-se estritamente nos arquivos de `/data/KPI/`. Se um valor excede o Teto de R$ 934,00, ele DEVE ser sinalizado.
2. **Janela Crítica:** Qualquer transação entre 18:00 e 08:00 recebe Score de Risco de 100%, conforme o arquivo 'estornos_pos_expediente.csv'.
3. **Zero Alucinação:** Se os dados da transação não constarem na base, atribua risco baseado apenas no Valor e Horário, informando que a Unidade é "Sem histórico de criticidade".
4. **Tom de Voz:** Profissional, analítico e direto. Use termos como "Ticket Médio", "Downtime de Segurança" e "Anomalia Transacional".
```

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolvemos um protótipo funcional que atua como o cockpit do Analista de Risco, integrando a inteligência da LLM com os dados históricos de Salvador e do ecossistema Bradesco.

- **Interface Interativa (Streamlit):** O front-end permite a entrada rápida de dados da transação (Valor, Loja, Horário) e retorna o Score de Risco visualmente (Verde, Amarelo ou Vermelho).
- **Integração com LLM:** O agente utiliza modelos de linguagem de última geração via API, configurados com baixa temperatura para garantir decisões determinísticas e técnicas.
- **Arquitetura RAG (Retrieval-Augmented Generation):** A aplicação não depende apenas do conhecimento geral da IA; ela realiza uma varredura nas pastas `/data/KPI/` antes de cada resposta, garantindo que o teto de **R$ 934,00** e a janela de **100% de fraude pós-expediente** sejam aplicados com precisão.


📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

A qualidade do **FraudGuard AI** é monitorada através de KPIs de performance de IA, garantindo que o agente atue como um filtro de segurança confiável para o ecossistema Bradesco.

#### 📊 Métricas de Performance

| Métrica | Descrição | Exemplo de Validação |
|:--- |:--- |:--- |
| **Precisão/Assertividade** | O agente identificou o risco real? | Estorno às 21h deve retornar **100% de risco** (conforme `estornos_pos_expediente.csv`). |
| **Taxa de Respostas Seguras** | O agente evitou alucinações? | Recusa em inventar senhas de gerentes ou limites de crédito fora do teto de **R$ 934,00**. |
| **Coerência de Negócio** | O veredito faz sentido operacional? | Bloqueio imediato para a **Loja 1**, que é o principal foco de perdas em Salvador. |

---

#### 🧪 Ciclo de Melhoria Contínua

Para garantir a confiabilidade do agente, estabelecemos um fluxo de avaliação em duas frentes:

1. **Testes de Estresse (Backtesting):** Rodamos o agente contra 10% da base histórica de 102.000 registros para validar se o Score de Risco gerado pela IA coincide com as fraudes já confirmadas no passado.
2. **Feedback do Analista de Risco:** O sistema permite que o usuário final atribua uma nota de 1 a 5 para a **Justificativa Técnica**. Notas baixas disparam um alerta para refinamento das instruções no `System Prompt`.

> [!TIP]
> Realizamos testes cegos com 3 usuários simulando o papel de "Analista de Fraudes" para validar se a interface em **Streamlit** e as respostas da IA são intuitivas e seguras para a tomada de decisão em tempo real.

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch (Roteiro de Apresentação)

> [!NOTE]
> O vídeo com a demonstração prática do agente será adicionado em breve. Abaixo, apresento a estrutura estratégica da solução.

#### **O Problema: O "Galo Cego" dos Estornos**
"Olá, eu sou o Victor Biscaia, Data Analyst & Engineer. Em operações de varejo e manutenção industrial, o maior risco financeiro não está na venda, mas no **estorno**. Analisando uma base de mais de **100.000 registros**, identifiquei que a fraude não é apenas uma questão de volume, mas de **criticidade**. Descobrimos, por exemplo, que 100% dos estornos realizados pós-expediente eram fraudulentos, mas sem uma IA, o analista humano não consegue cruzar esses padrões em tempo real para cada transação."

#### **A Solução: FraudGuard AI**
"Para resolver isso, desenvolvi o **FraudGuard AI**. Diferente de chatbots comuns, ele é um especialista de risco que utiliza a técnica de **RAG (Retrieval-Augmented Generation)**. Na prática, o agente funciona como um filtro inteligente que cruza três camadas de dados instantaneamente:
1. **Janela Temporal:** Bloqueio automático em horários de alta criticidade (18h-08h).
2. **Teto de Segurança:** Validação contra o limite histórico de **R$ 934,00**.
3. **Geolocalização de Risco:** Identificação de unidades críticas, como a **Loja 1** em Salvador.

O resultado é um **Score de Risco de 0 a 100%** com justificativa técnica baseada em evidências reais."

#### **O Diferencial Inovador**
"O grande diferencial desta solução é a **segurança e a ausência de alucinações**. O agente é restrito por diretrizes de compliance que o impedem de inventar dados, garantindo que cada decisão seja fundamentada nos KPIs reais da operação. Integramos Engenharia de Dados com IA Generativa para transformar dados brutos em decisões estratégicas, reduzindo o prejuízo financeiro e aumentando a eficiência operacional."

#### **Fechamento**
"Com o FraudGuard AI, a tecnologia deixa de ser apenas uma ferramenta de chat e passa a ser um defensor ativo do lucro da empresa. Convido você a testar o protótipo funcional aqui no repositório. Obrigado!"

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## 🛠️ Ferramentas Utilizadas

O projeto foi construído utilizando ferramentas líderes de mercado, focando em escalabilidade e baixo custo de implementação:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | **Gemini 1.5 Pro** (Cérebro do agente), [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/) (Interface), [Python](https://www.python.org/), [Google Colab](https://colab.research.google.com/) |
| **Engenharia de Dados** | **SQL** (Queries de extração), **Power BI** (Visualização de KPIs), **Pandas** (Tratamento de CSVs) |
| **Orquestração & RAG** | [LangChain](https://www.langchain.com/) (Integração de dados), [Git Bash](https://gitforwindows.org/) (Controle de Versão) |
| **Diagramas & Design** | [Mermaid](https://mermaid.js.org/) (Arquitetura), [Canva](https://www.canva.com/) (Branding PUNCH ROOTS) |

> [!TIP]
> A escolha do **Streamlit** permitiu transformar scripts de análise complexos em uma ferramenta visual acessível para gerentes que não possuem background técnico em dados.

---

## 📂 Estrutura do Repositório

```text
📁 dio-lab-fraudguard-ai/
│
├── 📄 README.md                      # Documentação principal do projeto
│
├── 📁 data/                          # Base de conhecimento para o RAG
│   ├── 📁 KPI/                       # Regras de negócio e métricas críticas
│   │   ├── estornos_pos_expediente.csv
│   │   ├── metricas_financeiras_fraude.csv
│   │   └── resumo_geral_kpi.csv
│   ├── Total de fraudes por loja.csv # Histórico geográfico de perdas
│   └── alarmes_industriais.csv       # Dados brutos para análise de correlação
│
├── 📁 docs/                          # Documentação detalhada
│   ├── 01-arquitetura-agente.md      # Fluxo de dados e lógica RAG
│   ├── 02-estrategia-dados.md        # Como os 102k registros foram tratados
│   ├── 03-engenharia-prompts.md      # Detalhamento do System Prompt
│   ├── 04-avaliacao-metricas.md      # Resultados de acurácia e segurança
│   └── 05-roteiro-pitch.md           # Roteiro para a apresentação final
│
├── 📁 src/                           # Código-fonte da aplicação
│   ├── app.py                        # Interface Streamlit do FraudGuard
│   └── engine.py                     # Lógica de conexão com a LLM
│
├── 📁 assets/                        # Identidade visual e diagramas
│   ├── logo-fraudguard.png
│   └── diagrama-arquitetura.mermaid
│
└── 📁 notebooks/                     # Exploração inicial de dados
    └── analise_exploratoria.ipynb    # SQL e Python para extração dos KPIs
```

---

## 👨‍💻 Autor

**Victor Biscaia** *Data Analyst & Engineer*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/victor-biscaia/)

🔗 [Acesse meu perfil profissional no LinkedIn](https://www.linkedin.com/in/victor-biscaia/)

---

### 🎓 Conclusão de Bootcamp
Este projeto é o resultado prático do **Bootcamp Bradesco - GenAI & Dados**, realizado em parceria com a **DIO**. A solução reflete a aplicação de engenharia de prompts, estruturação de bases de dados (RAG) e visão analítica para resolver desafios reais de segurança e conformidade financeira.

> **"Transformando dados brutos em decisões estratégicas e segurança operacional."** 🚀

---
_Dúvidas, feedbacks ou conexões? Vamos conversar pelo LinkedIn!_
