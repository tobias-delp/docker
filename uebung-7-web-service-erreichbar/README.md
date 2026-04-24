# Uebung 7: Web-Service erreichbar machen

Ziel: Ein Compose-Service soll vom Host im Browser erreichbar sein.

## Dateien

- `compose.yaml`: startet `nginx` mit Portfreigabe

## Schritte

1. `docker compose up -d`
2. `docker compose ps`
3. `http://localhost:8080` im Browser oeffnen

## Fragen

- Welcher Host-Port ist freigegeben?
- Welcher Container-Port wird angesprochen?
- Warum ist `web` trotzdem der interne Service-Name?

## Aufraeumen

```bash
docker compose down
```
