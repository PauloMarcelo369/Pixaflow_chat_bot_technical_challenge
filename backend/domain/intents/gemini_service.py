import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5")
GEMINI_API_URL = os.getenv("GEMINI_API_URL")

class GeminiService:
    def build_prompt(self, user_input: str) -> str:
        return f"""
Você é um analisador de intenções de um sistema de frutas.
Seu trabalho é transformar a pergunta do usuário em um JSON contendo:

- "intent": o nome da intenção que melhor representa a pergunta
- "parameters": dicionário com parâmetros relevantes (se houver)

Abaixo estão as intenções disponíveis e suas descrições detalhadas:

1. count_fruits
   - Descrição: Retorna o total de frutas cadastradas no sistema.
   - Parâmetros: nenhum

2. fruit_with_max_quantity
   - Descrição: Retorna a fruta que possui a maior quantidade disponível.
   - Parâmetros: nenhum

3. fruits_below_min_stock
   - Descrição: Lista todas as frutas cujo estoque atual é menor que o estoque mínimo definido.
   - Parâmetros: nenhum

4. get_fruit_info
   - Descrição: Retorna todas as informações disponíveis de uma fruta específica.
   - Parâmetros:
     - "name": nome da fruta (ex: "Banana")

5. summary
   - Descrição: Gera um resumo textual de todas as frutas cadastradas, incluindo quantidade, cores, origem, etc.
   - Parâmetros: nenhum

Regras importantes:
- Retorne **APENAS JSON válido**.
- Se não reconhecer a intenção, retorne:
  {{ "intent": "unknown", "parameters": {{}} }}
- Nunca responda em texto natural.

Exemplos de saída:

Pergunta: "Quantas frutas temos cadastradas?"
Resposta: {{ "intent": "count_fruits", "parameters": {{}} }}

Pergunta: "Me diga tudo sobre a Banana"
Resposta: {{ "intent": "get_fruit_info", "parameters": {{ "name": "Banana" }} }}

Pergunta do usuário:
"{user_input}"
"""
    
    
