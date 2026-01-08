# Fruit Chat - Projeto de Teste Técnico

Sistema de chat para interagir com informações sobre frutas. Permite perguntas sobre frutas cadastradas, estoques, categorias, estações, etc.

---

## 🛠️ Tecnologias usadas

- **Backend:** Python, FastAPI, SQLModel
- **Frontend:** React
- **Integração com IA:** Google Gemini (opcional, depende da cota)
- **Gerenciador de dependências (Python):** uv

---

## ⚡ Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone <https://github.com/PauloMarcelo369/Pixaflow_chat_bot_technical_challenge.git>
cd <nome-do-repo>
```

---

### 2. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do **backend** com o seguinte conteúdo:

```env
GEMINI_API_KEY=YOUR_API_KEY_AQUI
GEMINI_MODEL=gemini-1.5
DATABASE_URL=sqlite:///./data/fruit.db
```

> ⚠️ Caso não possua chave do Gemini ou a cota esteja esgotada, o sistema continuará funcionando com respostas de fallback.

---

### 3. Instalar dependências do backend com `uv`

Acesse a pasta do backend:

```bash
cd backend
```

Instale as dependências:

```bash
uv pip install -r requirements.txt
```

> ✅ Recomenda-se utilizar um ambiente virtual (`venv`), embora não seja obrigatório.

---

### 4. Rodar o backend

Ainda dentro da pasta `backend`, execute:

```bash
uv run main:app --reload
```

O backend estará disponível em:

```
http://127.0.0.1:8000
```

---

### 5. Instalar dependências do frontend

Acesse a pasta do frontend:

```bash
cd frontend
```

Instale as dependências:

```bash
npm install
```

---

### 6. Rodar o frontend

```bash
npm run dev
```

O frontend abrirá em:

```
http://localhost:5173
```

---

## 📝 Observações importantes

- Garanta que não haja outros processos rodando nas mesmas portas (`8000` e `5173`).
- O chat funciona **localmente mesmo sem Gemini**, retornando mensagens de fallback.
- Se a cota do Gemini estiver estourada, a IA não responderá, mas o backend e frontend continuarão funcionais.

---

## 💬 Exemplos de perguntas suportadas

- "Quantas frutas temos cadastradas?"
- "Me diga tudo sobre a Banana"
- "Quais frutas estão abaixo do estoque mínimo?"
- "Quais frutas da categoria Tropical?"
- "Quais frutas da estação Verão?"

---

## 🧠 Intents disponíveis no backend

- `count_fruits`
- `get_all`
- `fruit_with_max_quantity`
- `fruits_below_min_stock`
- `get_fruit_info`
- `get_fruits_by_category`
- `get_fruits_by_season`

---

## 📚 Enums úteis para pesquisa

### FruitCategory

```python
class FruitCategory(str, Enum):
    CITRUS = "citrus"
    TROPICAL = "tropical"
    BERRY = "berry"
    STONE = "stone"
    OTHER = "other"
    FRESH = "fresh"
```

### Season

```python
class Season(str, Enum):
    SUMMER = "summer"
    WINTER = "winter"
    AUTUMN = "autumn"
    SPRING = "spring"
    ALL_YEAR = "all_year"
```

---

## ✅ Considerações finais

Este projeto foi desenvolvido como parte de um teste técnico, priorizando clareza de arquitetura, separação de responsabilidades e facilidade de execução local.
