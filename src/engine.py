from groq import Groq

class FraudEngine:
    def __init__(self):
        # Chave de API da Groq validada
        self.api_key = "os.getenv("API_KEY")"
        self.client = Groq(api_key=self.api_key)
        
        # Modelo estável e de baixa latência
        self.model = "llama-3.1-8b-instant"

    def analisar(self, valor, loja, horario):
        # DIRETRIZES TÉCNICAS INQUESTIONÁVEIS (BASEADAS NO RELATÓRIO HISTÓRICO)
        contexto_seguranca = """
        DADOS DE AUDITORIA (HISTÓRICO REAL):
        1. UNIDADE LÍDER EM FRAUDES: A 'Loja 1' é a unidade mais crítica da rede. Concentra o maior prejuízo total (R$ 1.853,92) e a maior média por incidente (R$ 137,58).
        2. GRUPO DE ALTO RISCO: As unidades 1, 2, 3, 4, 5 e 6 concentram 100% das fraudes registradas. Todas as outras são seguras.
        3. JANELA OPERACIONAL: O expediente padrão é das 08:00 às 22:00.
        4. REGRA DE OURO (100% FRAUDE): Qualquer estorno realizado após as 22:00 é FRAUDE CONFIRMADA por histórico recorrente.
        5. TETO DE SEGURANÇA: A 'Loja 5' possui um limite operacional de R$ 934,00 para operações sem alerta.
        """

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": (
                            f"Você é o FraudGuard AI, especialista em cibersegurança. "
                            f"Use estritamente estes dados para sua análise: {contexto_seguranca}. "
                            "Sua resposta DEVE ser técnica e baseada no histórico. "
                            "Retorne: 1. Score de Risco (0-100%) e 2. Justificativa Técnica citando os valores do histórico."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"SOLICITAÇÃO -> Unidade: {loja}, Valor: R$ {valor}, Horário: {horario}",
                    }
                ],
                model=self.model,
                temperature=0.0, # Temperatura ZERO para eliminar qualquer alucinação ou 'chute'
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Erro na análise (Engine): {str(e)}"