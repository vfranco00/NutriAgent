# NutriAgent — Requisitos, Sprints e Entregas

> Backend com agente de IA para planejamento alimentar personalizado.

## 📚 Sumário
- [Visão Geral](#-visão-geral)
- [Requisitos Funcionais](#-requisitos-funcionais)
- [Requisitos Não Funcionais](#-requisitos-não-funcionais)
- [Planejamento de Sprints](#-planejamento-de-sprints)
- [Entregas por Sprint (DoD)](#-entregas-por-sprint-definition-of-done)
- [Critérios de Aceite](#-critérios-de-aceite)
- [Riscos & Premissas](#-riscos--premissas)
- [Próximos Passos](#-próximos-passos)
- [Especificações Técnicas](#-especificações-técnicas)
- [Como Rodar o Projeto](#️-como-rodar-o-projeto)
- [Verificação Rápida (cURL/Postman)](#-verificação-rápida-curlpostman)
- [Banco de Dados (psql)](#-banco-de-dados-psql)
- [Scripts Úteis (Makefile)](#-scripts-úteis-makefile)
- [Estrutura de Pastas (sugerida)](#-estrutura-de-pastas-sugerida)
- [Problemas Comuns (Troubleshooting)](#-problemas-comuns-troubleshooting)

---

## 🎯 Visão Geral
- **Objetivo:** gerar cardápios e listas de compras personalizadas a partir do perfil nutricional do usuário, com apoio de LLM.
- **Stack (MVP):** FastAPI • PostgreSQL • SQLAlchemy/Alembic • Docker • GitHub Actions • JWT/OAuth2
- **Conformidade:** LGPD (consentimento, minimização e direito ao esquecimento)
- **Público-alvo:** pessoas com rotina corrida que precisam de praticidade e variedade na alimentação.

---

## ✅ Requisitos Funcionais
1. **Autenticação & Usuários**
   - Cadastro, login via JWT, recuperação de senha
   - Perfis: usuário e admin (RBAC básico)
2. **Perfil Nutricional**
   - Preferências (gostos/aversões), restrições (alergias/intolerâncias)
   - Metas (emagrecimento, manutenção, ganho de massa)
3. **Receitas & Ingredientes**
   - CRUD de receitas e ingredientes com unidades (g, ml, colheres)
   - Cálculo automático de calorias e macronutrientes por porção
4. **Planejamento de Refeições**
   - Geração automática de **plano semanal (21 refeições)** pelo agente de IA
   - Travar/editar refeições e substituir pratos
5. **Lista de Compras**
   - Consolidação de ingredientes do plano semanal
   - Exportação em **CSV** e **PDF**
6. **Chat/Assistente de IA**
   - Ajustes do plano e dúvidas sobre receitas
   - Histórico por usuário
7. **Admin & Auditoria**
   - Painel de métricas, gerenciamento de usuários e logs
   - Gestão de termos e consentimento
8. **Integrações**
   - E-mail transacional (confirmação/reset)
   - Provider de LLM configurável por variável de ambiente

---

## 🛡️ Requisitos Não Funcionais
- **Desempenho**
  - P95 < **300 ms** em endpoints CRUD
  - P95 < **1,5 s** para geração de plano semanal
- **Disponibilidade**
  - Meta **99,5%** (MVP)
  - Backups diários; **RPO 24h** e **RTO 4h**
- **Segurança**
  - Hash de senhas (bcrypt/argon2), JWT com expiração/refresh
  - Rate limiting, validação forte de entrada, proteção a brute force
  - LGPD: consentimento, minimização, exclusão de dados
- **Escalabilidade & Infra**
  - Conteinerização (Docker); filas para tarefas pesadas e cache pontual
- **Observabilidade**
  - Logs estruturados (JSON), métricas (OpenTelemetry), tracing
- **Qualidade**
  - Testes unitários/integrados, **cobertura ≥ 70%** no MVP
  - CI com lint, testes e migrations

---

## 🗺️ Planejamento de Sprints (2 semanas)

| Sprint | Período (America/Sao_Paulo) | Objetivos-chave |
|---|---|---|
| **1** | **07–20/10/2025** | Setup do backend (FastAPI), estrutura, Docker, PostgreSQL; Auth/JWT, usuários; Alembic; seeds; CI básico |
| **2** | **21/10–03/11/2025** | CRUD de receitas/ingredientes e perfis; cálculos de macros; lista de compras inicial |
| **3** | **04–17/11/2025** | Integração LLM, prompts/guardrails; geração/edição de plano semanal; histórico de chat; exportações |
| **4** | **18/11–01/12/2025** | Hardening (segurança, LGPD), rate limit; observabilidade; tuning e guia de deploy |

---

## 📦 Entregas por Sprint (Definition of Done)

### ✅ Sprint 1 — Fundação do Backend
- [ ] Repositório organizado e **Docker Compose** funcional
- [ ] Banco com **migrations Alembic** + **seeds**
- [ ] **Auth/Users** operando (cadastro, login, /me)
- [ ] **OpenAPI** disponível e **CI** com lint/testes iniciais

### ✅ Sprint 2 — Domínio Core
- [ ] CRUD de **receitas**, **ingredientes** e **perfil nutricional**
- [ ] Cálculo validado de **macros** e **calorias**
- [ ] Scripts de **seed** e exemplos de payload
- [ ] **Cobertura de testes ≥ 60%**

### ✅ Sprint 3 — IA & Plano Semanal
- [ ] Provider de **LLM** configurável (env)
- [ ] **Geração do plano semanal** (21 refeições) e **edição**
- [ ] **Histórico** do chat por usuário
- [ ] **Exportações CSV/PDF** e cache pontual

### ✅ Sprint 4 — Hardening & Deploy
- [ ] **Rate limiting**, validações e políticas LGPD
- [ ] **Logs, métricas e tracing** com dashboards
- [ ] Guia de **deploy** e **Release Candidate** tagueado

---

## 🧪 Critérios de Aceite
- **Autenticação**  
  *Dado* um usuário cadastrado, *quando* loga com credenciais válidas, *então* recebe JWT e acessa **/me**.

- **Plano Semanal**  
  *Dadas* preferências e metas, *quando* solicita plano, *então* recebe **21 refeições** com macros por dia.

- **Lista de Compras**  
  *Dado* um plano gerado, *quando* exporta, *então* obtém **CSV/PDF** com totais por ingrediente.

- **LGPD — Exclusão**  
  *Dado* um pedido de exclusão, *quando* confirmado, *então* dados pessoais são removidos e acesso revogado.

---

## ⚠️ Riscos & 📌 Premissas
**Riscos**
- Custos/limites do provider de LLM impactarem latência/orçamento
- Dados de receitas inconsistentes afetarem cálculos
- Crescimento de escopo em features de IA (scope creep)

**Premissas**
- Equipe com acesso a Docker e PostgreSQL
- Contas ativas para e-mail transacional e LLM
- Sprints quinzenais com cerimônias ágeis

---

## ▶️ Próximos Passos
1. Refinar backlog em **épicos → histórias → tarefas** com estimativas
2. Priorizar épicos do **MVP**
3. Definir **staging** e pipeline de **deploy**
4. Fixar métricas de **P95**, **cobertura** e **disponibilidade**

---

## 🔧 Especificações Técnicas

### Stack e versões (sugeridas)
- **Linguagem:** Python 3.11+
- **Web Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **ORM:** SQLAlchemy 2.x + Alembic (migrations)
- **Banco de Dados:** PostgreSQL 16
- **Autenticação:** OAuth2 + JWT (PyJWT)
- **Testes:** Pytest + Coverage
- **Qualidade:** Ruff (lint), Black (format), MyPy (types)
- **Containerização:** Docker & Docker Compose
- **CI/CD:** GitHub Actions (lint, testes, migrations)
- **Observabilidade:** Logs estruturados (JSON), OpenTelemetry (métricas/tracing opcional)

### Arquitetura (alto nível)
- **app/**
  - `main.py` – ponto de entrada do FastAPI (inclui routers e middlewares)
  - `core/` – configs globais (settings, security, logging)
  - `db/` – engine, sessão, base declarativa, repositórios
  - `models/` – modelos SQLAlchemy
  - `schemas/` – Pydantic (request/response)
  - `routers/` – controladores (auth, users, recipes, plans, admin, etc.)
  - `services/` – regras de negócio (IA, cálculo de macros, lista de compras)
  - `llm/` – clients e prompts; provider configurável via env
  - `utils/` – helpers (e-mail, pdf/csv export, rate limiting)
- **migrations/** – versões do Alembic
- **tests/** – testes unitários e integrados
- **docker/** – arquivos de infra (Dockerfile, compose, entrypoints)

### Principais Endpoints (exemplos)
- `POST /auth/signup`, `POST /auth/login`, `GET /auth/me`
- `GET/POST/PUT/DELETE /recipes`, `GET /recipes/{id}`
- `GET/POST /ingredients`
- `POST /plan/generate` (gera 7 dias/21 refeições)
- `GET /shopping-list/export?format=csv|pdf`
- `GET /chat/history`, `POST /chat/message`
- `DELETE /admin/user/{id}` (RBAC: admin)

### Variáveis de Ambiente (.env — exemplo)
```
# Banco
DATABASE_URL=postgresql+psycopg://nutri:nutri@db:5432/nutri

# JWT
JWT_SECRET=troque-este-segredo
JWT_EXPIRES_MINUTES=60
JWT_ALGORITHM=HS256

# E-mail (opcional)
MAIL_HOST=smtp.example.com
MAIL_PORT=587
MAIL_USERNAME=seu_usuario
MAIL_PASSWORD=sua_senha
MAIL_FROM=noreply@nutriagent.app
MAIL_TLS=true

# LLM (opcional)
LLM_PROVIDER=openai
OPENAI_API_KEY=xxxx

# App
APP_ENV=development
LOG_LEVEL=INFO
```

> **Dica:** Em dev local sem Docker, troque o host para `localhost` no `DATABASE_URL`.

### Padrões de Código
- **Lint:** `ruff check .`
- **Format:** `black .`
- **Tipos:** `mypy app`

### Testes
- **Executar:** `pytest -q`
- **Cobertura:** `coverage run -m pytest && coverage report -m`

---

## ▶️ Como rodar o projeto

> Escolha **Docker** (recomendado) ou **ambiente local** (Python).

### Opção A — Docker (One-liner)
Requisitos: Docker + Docker Compose

```bash
# 1) Copie .env.example para .env e ajuste as variáveis
cp .env.example .env   # se existir; senão crie manualmente

# 2) Suba os serviços (API + Postgres)
docker compose up -d --build

# 3) Rode as migrations dentro do container da API
docker compose exec api alembic upgrade head

# 4) (Opcional) rode seeds/dados de exemplo
docker compose exec api python -m app.seed

# 5) Acesse a API
# Swagger UI: http://localhost:8000/docs
# OpenAPI JSON: http://localhost:8000/openapi.json
```

**Atalhos úteis**
```bash
# Logs
docker compose logs -f api

# Reiniciar API
docker compose restart api

# Derrubar tudo
docker compose down -v
```

### Opção B — Ambiente local (Python)
Requisitos: Python 3.11+, PostgreSQL 16

```bash
# 1) Crie e ative o virtualenv
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# 2) Instale dependências
pip install -U pip
pip install -r requirements.txt

# 3) Exporte as variáveis de ambiente (ou use um .env com python-dotenv)
# macOS/Linux:
export DATABASE_URL="postgresql+psycopg://nutri:nutri@localhost:5432/nutri"
export JWT_SECRET="troque-este-segredo"
# Windows (PowerShell):
setx DATABASE_URL "postgresql+psycopg://nutri:nutri@localhost:5432/nutri"
setx JWT_SECRET "troque-este-segredo"

# 4) Crie o banco (se necessário) e rode as migrations
alembic upgrade head

# 5) (Opcional) seeds
python -m app.seed

# 6) Suba a API
uvicorn app.main:app --reload --port 8000

# Acesse:
# http://localhost:8000/docs
```

---

## 🔎 Verificação Rápida (cURL/Postman)
```bash
# Signup
curl -X POST http://localhost:8000/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"Senha@123","name":"User"}'

# Login (obtenha access_token)
TOKEN=$(curl -s -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"Senha@123"}' | jq -r .access_token)

# /me autenticado
curl http://localhost:8000/auth/me -H "Authorization: Bearer $TOKEN"
```

---

## 🗄️ Banco de Dados (psql)
```bash
# Via Docker
docker compose exec db psql -U nutri -d nutri

# Local
psql -h localhost -U nutri -d nutri
```

---

## 🧰 Scripts Úteis (Makefile)
```bash
make up        # sobe docker compose
make migrate   # alembic upgrade head
make seed      # popular dados iniciais
make test      # pytest
make down      # docker compose down -v
```

---

## 🗂️ Estrutura de Pastas (sugerida)
```
.
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── settings.py
│   │   ├── security.py
│   │   └── logging.py
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── repositories/
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── recipes.py
│   │   ├── ingredients.py
│   │   ├── plans.py
│   │   └── admin.py
│   ├── services/
│   │   ├── plan_service.py
│   │   └── shopping_list_service.py
│   ├── llm/
│   │   ├── provider.py
│   │   └── prompts.py
│   └── utils/
│       ├── email.py
│       ├── export_csv.py
│       └── export_pdf.py
├── migrations/
├── tests/
├── docker/
│   ├── Dockerfile
│   └── entrypoint.sh
├── docker-compose.yml
├── alembic.ini
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🆘 Problemas Comuns (Troubleshooting)
- **`Connection refused` no Postgres:** aguarde o container `db` iniciar ou revise `DATABASE_URL`.
- **Migrations não rodam:** verifique `alembic.ini` e `target_metadata` do seu `Base`.
- **JWT inválido/expirado:** gere novo token com `/auth/login` e confira `JWT_EXPIRES_MINUTES`.
- **CORS em frontend:** habilite middleware CORS em `app/main.py` com origins do seu front.
- **Erro ao exportar PDF/CSV:** confirme libs/bibliotecas instaladas e permissões de escrita (pasta temp/exports).
