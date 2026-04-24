# Uebung 10: Compose Setup debuggen

Ziel: Ein laufendes, aber fehlerhaftes Compose-Setup systematisch analysieren.

## Situation

Der Container startet, aber unter `http://localhost:8083` erscheint nicht die erwartete Startseite.

## Dateien

- `compose.yaml`: startet den Service `web`
- `web/Dockerfile`: baut ein kleines nginx-Image
- `web/public/home.html`: absichtlich keine `index.html`

## Schritte

1. `docker compose up --build`
2. `http://localhost:8083` im Browser oeffnen
3. `docker compose logs web`
4. `docker compose exec web sh`
5. `ls -la /usr/share/nginx/html`

## Leitfragen

- Laeuft der Container?
- Welche Dateien liegen im Web-Root?
- Warum liefert nginx nicht die erwartete Startseite?
- Welche minimale Aenderung wuerde das Problem beheben?

## Erwartete Ursache

Im Web-Root liegt `home.html`, aber keine `index.html`.

## Aufraeumen

```bash
docker compose down
```
