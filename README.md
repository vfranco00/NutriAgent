# NutriAgent – README (Sprints & Especificações)

Este repositório contém o **backend** do NutriAgent. O objetivo é construir uma API para gestão de preferências alimentares e, nas próximas sprints, integrar um **agente de IA** para busca/geração de receitas e planejamento nutricional.

---

## 🗓️ Planejamento por Sprints

### Sprint 1 — Fundação do Backend & DB (ENTREGUE)
**Escopo**
- Stack básica (FastAPI + PostgreSQL + SQLAlchemy + Alembic).
- Autenticação: signup/login com JWT (bcrypt para senhas).
- Domínios iniciais: `users`, `foods`, `dietary_preferences`.
- Migrações de banco; documentação Swagger habilitada.

**Entregáveis**
- Rotas: `/auth/signup`, `/auth/login`, `/foods`, `/preferences` (detalhes no código).
- Migrations aplicadas e base de dados criada.

**Critérios de Aceite**
- Criar usuário e logar com sucesso (JWT emitido).
- CRUD básico de `foods` protegido por JWT.
- Criar e listar `dietary_preferences` do usuário autenticado.
- Projeto roda localmente via Docker + Uvicorn.

**Fora do escopo (nesta sprint)**
- `recipes`, `recipe_ingredients`, cálculo de macros, agente de IA.

---

### Sprint 2 — Receitas & Macros (PLANEJADA)
- Modelos e CRUD de `recipes` e `recipe_ingredients`.
- Serviço de cálculo de macros/calorias por porção/total.
- Busca textual e filtros (custo/dificuldade).

### Sprint 3 — Agente de IA (PLANEJADA)
- Integração de embeddings (pgvector) e busca semântica.
- Ferramentas do agente (buscar receitas, ajustar porções, validar restrições).
- Endpoints: `/planner/plan-day`, `/recipes/generate` (validação e persistência).

### Sprint 4 — Hardening & Preparação do Front (PLANEJADA)
- Paginação, logs, dataset de exemplo maior, documentação de consumo.
- Endpoints para recuperar planos por data e refino de erros.

---

## ⚙️ Especificações Técnicas

- **Linguagem**: Python **3.11+**
- **Framework**: FastAPI
- **Banco de dados**: PostgreSQL **16** (via Docker)
- **ORM & Migrações**: SQLAlchemy + Alembic
- **Autenticação**: JWT (HS256) + `passlib[bcrypt]`
- **Configuração**: `.env` com `pydantic-settings`
- **Servidor dev**: Uvicorn (reload)

> Opcional recomendado: `ruff`/`black` e `pre-commit` para qualidade de código.

---

## 📁 Estrutura de Pastas (Sprint 1)

```
nutriagent/
├─ .gitignore
├─ .env.example
├─ docker-compose.yml
├─ requirements.txt
├─ README.md
├─ alembic.ini
├─ app/
│  ├─ main.py
│  ├─ core/
│  │  ├─ config.py
│  │  ├─ security.py
│  │  └─ deps.py
│  ├─ db/
│  │  ├─ session.py
│  │  └─ base.py
│  ├─ models/
│  │  ├─ user.py
│  │  ├─ food.py
│  │  └─ preference.py
│  ├─ schemas/
│  │  ├─ auth.py
│  │  ├─ user.py
│  │  ├─ food.py
│  │  └─ preference.py
│  ├─ crud/
│  │  ├─ user.py
│  │  ├─ food.py
│  │  └─ preference.py
│  └─ routers/
│     ├─ auth.py
│     ├─ foods.py
│     └─ preferences.py
└─ alembic/
   ├─ env.py
   └─ versions/
```

> Nota: nesta sprint cada modelo usa seu próprio `Base` (metadatas separadas). O `alembic/env.py` está configurado para migrar cada metadata em sequência.

---

## 🔐 Variáveis de Ambiente

Crie um `.env` a partir do exemplo:
```
cp .env.example .env
```

`.env.example`:
```
DB_URL=postgresql+psycopg2://nutri:nutri@localhost:5432/nutri
JWT_SECRET=troque-isto
JWT_EXPIRES_MIN=1440
```

---

## ▶️ Como Rodar (Dev)

1) **Ativar venv e instalar dependências**
```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
# .venv\Scripts\activate
pip install -r requirements.txt
```

2) **Subir PostgreSQL via Docker**
```bash
docker compose up -d
```

3) **Migrations (Alembic)**
```bash
# se ainda não existir
alembic init alembic
# garantir que alembic.ini e alembic/env.py são os do projeto
alembic revision --autogenerate -m "init tables"
alembic upgrade head
```

4) **Rodar a API**
```bash
uvicorn app.main:app --reload
```
- Healthcheck: http://127.0.0.1:8000/
- Swagger: http://127.0.0.1:8000/docs

---

## 🔧 Comandos Úteis

- Atualizar DB após mudanças de modelo:
```bash
alembic revision --autogenerate -m "update schema"
alembic upgrade head
```
- Reset (cuidado: destrói dados do volume local):
```bash
docker compose down -v && docker compose up -d
alembic upgrade head
```

---

## 🧱 Convenção de Commits (Sprint 1)

1. `chore: init repo, requirements, gitignore, readme`
2. `chore: add docker-compose and env example`
3. `feat(api): fastapi skeleton with root endpoint`
4. `feat(db): settings and session`
5. `feat(models): user, food, preference`
6. `feat(auth): security, schemas and signup/login routes`
7. `feat(foods): CRUD endpoints`
8. `feat(prefs): endpoints for dietary preferences`
9. `chore(migrations): alembic init and env config`

---

## ✅ Checklist da Sprint 1

- [ ] Signup/login emitindo JWT
- [ ] CRUD básico de foods (protegido)
- [ ] Preferências do usuário (criar/listar)
- [ ] Migrações aplicadas e banco operacional
- [ ] API acessível com docs em `/docs`

---

## 🗺️ Próximos Passos (Visão Geral)
- Sprint 2: `recipes`, `recipe_ingredients` e cálculo de macros.
- Sprint 3: agente de IA (RAG + pgvector) e planejamento diário.
- Sprint 4: hardening, paginação, logs e dataset de exemplo.
