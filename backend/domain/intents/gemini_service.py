import os
import json
from google import genai
from google.genai import types # For configuration types
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

client = genai.Client(api_key=GEMINI_API_KEY)

class GeminiService:
    def __init__(self):
        self.model_id = GEMINI_MODEL

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
5. get_all
    - retorna todas as frutas disponíveis no catálogo
    - Parâmetro: nenhum

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
    
    def parse_response(self, text: str) -> dict:
        clean_text = text.replace("```json", "").replace("```", "").strip()
        try:
            return json.loads(clean_text)
        except json.JSONDecodeError:
            print(f"Erro ao parsear JSON: {text}")
            return {"intent": "unknown", "parameters": {}}
    
    def get_intent(self, user_input: str) -> dict:
        try:
            prompt = self.build_prompt(user_input)
            
            response = client.models.generate_content(
                model=self.model_id,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type='application/json',
                    temperature=0.1,
                    max_output_tokens=200
                )
            )
            print("esse daqui é o response: ", response.text)
            if response.text:
                return self.parse_response(response.text)
            return {"intent": "unknown", "parameters": {}}
                    
        except Exception as e:
            print(f"Erro ao chamar Gemini API: {e}")
            return {"intent": "unknown", "parameters": {}}
