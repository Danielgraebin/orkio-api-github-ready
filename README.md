# Orkio API — FastAPI (GitHub + Railway)

## Requisitos
- Python 3.11+ (para rodar local)
- Docker (para build de produção)

## Rodando local
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
# http://localhost:8000/api/v1/health
```

## Docker local
```bash
docker build -t orkio-api .
docker run -p 8080:8080 -e OPENAI_API_KEY=sk-... -e JWT_SECRET=<secret> orkio-api
# http://localhost:8080/api/v1/health
```

## Variáveis de ambiente
- `OPENAI_API_KEY` (obrigatório) — nunca exponha no cliente
- `JWT_SECRET` (obrigatório)
- `ALLOWED_ORIGINS` (ex.: `https://orkio.app,https://admin.orkio.app`)

## Deploy no Railway (via GitHub)
1. Crie repo **orkio-api** e faça push.
2. No Railway: **New Project → Deploy from GitHub** (selecione este repo).
3. Configure as Variables: `OPENAI_API_KEY`, `JWT_SECRET`, `ALLOWED_ORIGINS`.
4. Deploy automático em push para `main`.

### (Opcional) Deploy via GitHub Actions
Configure **secrets** no repositório:
- `RAILWAY_TOKEN`
- `RAILWAY_PROJECT_ID`
- `RAILWAY_SERVICE_ID`
O workflow `.github/workflows/ci.yml` já dispara o deploy após o build/test.

## Endpoints principais
- `GET /api/v1/health`
- `POST /api/v1/auth/login`
- `POST /api/v1/agents/threads`
- `POST /api/v1/agents/messages`
