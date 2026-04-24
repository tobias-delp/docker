# Uebung 9: Eigenes Dockerfile mit Compose nutzen

Ziel: Ein eigenes Image per `build` zusammen mit einem zweiten Service starten.

## Dateien

- `compose.yaml`: startet `app` und `redis`
- `app/Dockerfile`: baut die Flask-Anwendung
- `app/app.py`: kleine Webanwendung
- `app/requirements.txt`: Python-Abhaengigkeiten

## Schritte

1. `docker compose up --build`
2. `docker compose ps`
3. `docker compose logs app`
4. `http://localhost:5001` im Browser oeffnen

## Fragen

- Wird `app` gebaut oder heruntergeladen?
- Welche Rolle spielt `build: ./app`?
- Welche Logs schreibt die Anwendung?

## Aufraeumen

```bash
docker compose down
```
