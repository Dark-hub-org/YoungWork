# Effective Mobile Test Task

Минимальное решение тестового задания на позицию DevOps.

## Структура проекта

```text
.
├── backend/
│   ├── app.py
│   └── Dockerfile
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

## Как запустить

Из корня проекта выполните:

```bash
docker compose up --build
```

Если у вас используется старая команда Compose:

```bash
docker-compose up --build
```

## Как проверить результат

После запуска выполните:

```bash
curl http://localhost
```

Ожидаемый ответ:

```text
Hello from Effective Mobile!
```

## Как работает схема

- `backend` запускает простой HTTP-сервер на Python на порту `8080`.
- `backend` доступен только внутри Docker-сети и не публикуется на хост.
- `nginx` принимает HTTP-запросы на порт `80` и проксирует их на `backend`.

Схема:

```text
Client -> nginx:80 -> backend:8080
```

## Технологии

- Docker
- Docker Compose
- Python standard library
- Nginx
