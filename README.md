# NutriAgent — Requisitos, Sprints e Entregas

> Backend com agente de IA para planejamento alimentar personalizado.

## 🎯 Visão Geral (bem breve)
- **Objetivo:** gerar cardápios e listas de compras personalizadas a partir do perfil nutricional do usuário, com apoio de LLM.
- **Stack (MVP):** FastAPI • PostgreSQL • SQLAlchemy/Alembic • Docker • GitHub Actions • JWT/OAuth2
- **Conformidade:** LGPD (consentimento, minimização e direito ao esquecimento)

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

| Sprint | Período | Objetivos-chave |
|---|---|---|
| **1** | **07–20/10/2025** | Setup do backend (FastAPI), estrutura, Docker, PostgreSQL; Auth/JWT, usuários; Alembic; seeds; CI básico |
| **2** | **21/10–03/11/2025** | CRUD de receitas/ingredientes e perfis; cálculos de macros; lista de compras inicial |
| **3** | **04–17/11/2025** | Integração LLM, prompts/guardrails; geração/edição de plano semanal; histórico de chat; exportações |
| **4** | **18/11–01/12/2025** | Hardening (segurança, LGPD), rate limit; observabilidade; tuning e guia de deploy |

> *Datas em America/Sao_Paulo.*

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

## 🧪 Critérios de Aceite (amostras)

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
