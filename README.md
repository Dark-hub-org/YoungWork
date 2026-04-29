## Структура проекта

```text
.
├── backend/
│   └── app.py
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## Как запустить

```bash
docker compose up --build
```

```bash
docker-compose up --build
```

```bash
curl http://localhost
```

## Процесс

- `backend` запускает простой HTTP-сервер на Python на порту `8080`.
- `backend` доступен только внутри Docker-сети и не публикуется на хост.
- `nginx` принимает HTTP-запросы на порт `80` и проксирует их на `backend`.

Схема:

```text
Client -> nginx:80 -> backend:8080
```
