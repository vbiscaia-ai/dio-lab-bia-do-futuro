# Base de Conhecimento

## Dados Utilizados

## 📁 Dados Utilizados

O **FraudGuard AI** utiliza uma arquitetura de dados estruturada para alimentar seu motor de decisão. Os arquivos estão organizados para separar métricas estratégicas de dados operacionais, garantindo alta precisão no processo de **RAG (Retrieval-Augmented Generation)**.

### 📂 Pasta: `/data/KPI/`
*Estes arquivos contêm os indicadores consolidados que definem as regras de peso e criticidade do agente:*

| Arquivo | Formato | Utilização no Agente |
|:---|:---:|:---|
| `resumo_geral_transacoes.csv` | CSV | Fornece o baseline da operação (517 transações) e a taxa média de fraude de **22,44%**. |
| `estornos_pos_expediente.csv` | CSV | Define a regra de **Risco Crítico (100%)** para transações e estornos fora do horário comercial. |
| `metricas_financeiras_fraude.csv` | CSV | Parametriza limites de valor, como o Ticket Médio (**R$ 126**) e o teto histórico (**R$ 934**). |

### 📂 Pasta: `/data/` (Arquivos de Suporte)
*Dados detalhados utilizados para cruzamento de informações e diagnósticos específicos:*

| Arquivo | Formato | Utilização no Agente |
|:---|:---:|:---|
| `total_de_fraudes_por_loja.csv` | CSV | Identifica a **Loja 1** e outras 5 unidades como focos de 100% das ocorrências de fraude. |
| `heatmap_horario_compras.csv` | CSV | Permite à IA entender a distribuição temporal e sazonal das tentativas de fraude. |
| `tempo_ate_estorno_fraude.csv` | CSV | Analisa o comportamento do "lead time" para diferenciar erros de digitação de ataques deliberados. |
| `deteccao-fraude-estorno.csv` | CSV | Base histórica completa utilizada para validação de padrões comportamentais complexos. |

---

### 🧠 Lógica de Processamento de Dados
O agente foi instruído a seguir uma hierarquia de consulta:
1. **Prioridade Máxima:** Dados da pasta `/KPI/` (Regras de Ouro).
2. **Contextualização:** Dados da pasta `/data/` (Refinamento do diagnóstico).
3. **Saída:** Geração de Score baseado na evidência estatística encontrada nos arquivos acima.

## Estratégia de Integração

## 🔌 Estratégia de Integração

### Como os dados são carregados?

O **FraudGuard AI** utiliza uma arquitetura de carregamento híbrida para garantir que a IA tome decisões baseadas em fatos reais, e não em suposições:

* **Ingestão Iniciais (Cold Start):** Ao iniciar a sessão no **Streamlit**, os arquivos consolidados da pasta `/data/KPI/` são carregados em memória via **Pandas**. Os principais indicadores (Taxa de 22,44%, Regra dos 100% Pós-Expediente e Ticket Médio) são injetados diretamente no **System Prompt** para garantir que a IA nunca perca o contexto das "Regras de Ouro".
* **Recuperação Contextual (RAG):** Quando o analista insere os dados de uma transação (ex: Loja 1, Valor R$ 500), o sistema realiza uma busca nos arquivos de suporte na pasta `/data/`. Se houver correspondência com o ranking de unidades críticas ou padrões de horários, esse trecho específico do CSV é convertido em texto e enviado como contexto adicional para a **LLM**.
* **Processamento e Resposta:** A LLM (GPT-4o/Gemini) processa os dados da transação cruzando-os com os arquivos carregados e gera o diagnóstico final, citando qual arquivo serviu de base para aquela decisão específica.

---

### 🔄 Ciclo de Vida da Informação
1. **Entrada:** Analista fornece ID da Loja, Valor e Horário.
2. **Busca:** Script Python filtra os arquivos `/data/KPI/` e `/data/`.
3. **Augmentation:** O prompt é "enriquecido" com os dados encontrados.
4. **Geração:** A IA retorna o Score de Risco e a justificativa técnica.

### Como os dados são usados no prompt?

A integração dos dados no prompt ocorre de forma **híbrida (Estática + Dinâmica)** para maximizar a precisão e minimizar o consumo de tokens:

1.  **System Prompt (Estático - Regras de Ouro):** Os indicadores macro extraídos da pasta `/data/KPI/` (como a taxa de 22,44% e o teto de R$ 934) são inseridos diretamente nas instruções do sistema. Isso garante que a IA tenha uma "consciência" constante dos limites operacionais, independentemente da pergunta do usuário.

2.  **Contexto Dinâmico (RAG - Consulta sob Demanda):** Quando o analista insere dados de uma transação específica, o sistema realiza uma filtragem prévia nos arquivos da pasta `/data/`. 
    * *Exemplo:* Se o usuário informa "Loja 1", o script localiza a linha correspondente no arquivo `total_de_fraudes_por_loja.csv` e injeta apenas essa informação no prompt: *"Contexto Adicional: A Loja 1 possui um histórico de X fraudes, representando Y% do prejuízo total."*

3.  **Few-Shot Prompting (Exemplos):** Utilizamos exemplos reais de estornos fraudulentos (baseados no arquivo `deteccao-fraude-estorno.csv`) para ensinar à IA a diferença sutil entre um comportamento legítimo e um padrão de ataque, guiando o raciocínio da LLM antes dela gerar o veredito.

---

**Fluxo de Montagem do Prompt:**
> **Instrução do Sistema** (Regras de Ouro dos KPIs) 
> \+ **Contexto Recuperado** (Dados específicos da Loja/Horário filtrados dos CSVs) 
> \+ **Entrada do Usuário** (Dados da transação atual) 
> **= Diagnóstico de Precisão.**
---

## 📝 Exemplo de Contexto Montado

Abaixo, um exemplo de como o sistema estrutura os dados históricos e os indicadores de KPI para que a LLM processe a decisão:

```text
--- REGRAS DE OURO (KPIs ESTRATÉGICOS) ---
- Taxa Média de Fraude da Operação: 22,44% (Base: 517 transações)
- Janela de Risco Crítico: Pós-expediente (Incidência de 100% de fraude em 116 registros)
- Parâmetros Financeiros: Média R$ 126,00 | Teto Histórico R$ 934,00

--- DADOS DA TRANSAÇÃO ATUAL ---
- ID da Unidade: Loja 1
- Horário da Solicitação: 20:45 (Fora do expediente comercial)
- Valor do Estorno: R$ 450,00
- Tipo de Operação: Estorno de Compra Online

--- CONTEXTO RECUPERADO (RAG) ---
- Histórico da Unidade: A Loja 1 está no TOP 1 de criticidade, concentrando a maior parte do volume financeiro de perdas.
- Alerta Temporal: O horário de 20:45 coincide com o padrão de 100% de fraude identificado no arquivo 'estornos_pos_expediente.csv'.
- Desvio Financeiro: O valor de R$ 450,00 está 257% acima da média operacional (R$ 126,00).

--- INSTRUÇÃO FINAL ---
Analise os dados acima e forneça o Score de Risco e a recomendação de bloqueio.
