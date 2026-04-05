# 📊 Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do **FraudGuard AI** é realizada de duas formas complementares para garantir a segurança das operações financeiras:

1. **Testes Estruturados (Benchmark de Risco):**
   Definimos cenários de teste baseados nos KPIs reais de `/data/KPI/`. O agente é testado com entradas específicas para validar se ele respeita os limites críticos:
   * **Entrada:** Estorno às 19:30. **Resposta Esperada:** Risco 100% (Baseado em `estornos_pos_expediente.csv`).
   * **Entrada:** Valor R$ 1.000,00. **Resposta Esperada:** Alerta de Teto Excedido (Baseado no limite de R$ 934,00).
   * **Entrada:** Unidade 1. **Resposta Esperada:** Identificação como unidade de alta criticidade.

2. **Feedback Real (Validação do Analista):**
   Especialistas de risco e usuários do sistema testam o agente em situações do dia a dia e atribuem notas de 1 a 5 baseadas em:
   * **Precisão:** O Score de Risco condiz com a realidade da operação?
   * **Justificativa:** A explicação técnica foi clara e citou os dados corretos da base de conhecimento?
   * **Confiança:** O agente evitou alucinações e manteve-se restrito às regras de compliance?

---

## ⚖️ Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente identificou o risco corretamente? | Informar estorno às 21h e receber Score de 100% (Fraude Confirmada). |
| **Segurança** | O agente evitou inventar limites financeiros? | Perguntar o limite de crédito do gerente e o agente recusar por falta de acesso a dados sensíveis. |
| **Coerência** | A justificativa condiz com os KPIs da base? | Sinalizar risco alto para valores acima de R$ 934, citando o teto de segurança operacional. |

---

## 🧪 Exemplos de Cenários de Teste

Utilize estes testes simples para validar se o **FraudGuard AI** está operando conforme as regras de negócio estabelecidas:

### Teste 1: Validação de Janela Crítica (Horário)
- **Pergunta:** "Analise um estorno de R$ 50,00 na Loja 2 realizado às 22:30."
- **Resposta esperada:** Score de Risco de 100% com justificativa baseada no arquivo `estornos_pos_expediente.csv`.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 2: Validação de Teto de Segurança (Valor)
- **Pergunta:** "Qual o risco de um estorno de R$ 1.500,00 na Loja 5 às 10:00 da manhã?"
- **Resposta esperada:** Alerta de risco elevado (acima de 80%) por exceder o teto histórico de R$ 934,00 detalhado em `metricas_financeiras_fraude.csv`.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 3: Consulta de Unidade de Risco
- **Pergunta:** "Quais são as unidades com maior volume de fraudes registradas na base?"
- **Resposta esperada:** Identificação da **Loja 1** como a unidade crítica, conforme os dados de `Total de fraudes por loja.csv`.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [Liste aqui]

**O que pode melhorar:**
- [Liste aqui]

---

## ⚙️ Métricas Avançadas (Opcional)

Para elevar o nível de maturidade do **FraudGuard AI**, monitoramos métricas técnicas de observabilidade que garantem a eficiência do sistema em produção:

- **Latência e Tempo de Resposta:** Tempo total entre a submissão dos dados da transação e a geração do veredito de risco (meta: < 2.5s).
- **Consumo de Tokens e Custos:** Monitoramento do volume de tokens enviados no contexto (RAG) para otimizar o custo por análise de fraude.
- **Logs e Taxa de Erros:** Rastreio de falhas na leitura dos arquivos CSV em `/data/KPI/` e tratamento de exceções para garantir disponibilidade 24/7.

Ferramentas especializadas em LLMs, como **LangWatch** e **LangFuse**, são excelentes aliadas para esse monitoramento. No desenvolvimento deste projeto, o foco foi garantir que a recuperação dos dados (**Retrieval**) fosse precisa para alimentar o prompt de decisão de forma limpa e eficiente.
