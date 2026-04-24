# Uebung 6: Erstes Compose Setup

Ziel: Zwei fertige Services mit Docker Compose gemeinsam starten.

## Dateien

- `compose.yaml`: startet `nginx` und `redis`

## Schritte

1. `docker compose up -d`
2. `docker compose ps`
3. `docker ps`

## Fragen

- Welche Container laufen?
- Welche Servicenamen wurden vergeben?
- Welche Images werden verwendet?

## Aufraeumen

```bash
docker compose down
```
