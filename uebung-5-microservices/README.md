# Uebung 5: Transfer zu Microservices

Ziel: Mehrere Services mit getrennten Dockerfiles betrachten.

## Struktur

- `frontend`: statische Startseite mit nginx
- `user-service`: kleiner Flask-Service fuer Benutzerdaten
- `order-service`: kleiner Flask-Service fuer Bestellungen

## Beispielbefehle

### Frontend

```bash
cd frontend
docker build -t ms-frontend .
docker run -p 8082:80 ms-frontend
```

### User Service

```bash
cd user-service
docker build -t user-service .
docker run -p 5001:5000 user-service
```

### Order Service

```bash
cd order-service
docker build -t order-service .
docker run -p 5002:5000 order-service
```

## Diskussionsfragen

- Warum hat jeder Service ein eigenes Dockerfile?
- Welche Dateien braucht jeder Service wirklich?
- Warum waere ein einziges grosses Image unpraktisch?
