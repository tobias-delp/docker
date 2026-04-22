# Uebung 3: Eigene HTML-Seite containerisieren

Ziel: Ein eigenes Image mit einem sehr einfachen Dockerfile bauen.

## Dateien

- `index.html`: einfache statische Seite
- `Dockerfile`: baut ein nginx-basiertes Image

## Schritte

1. `docker build -t team-page .`
2. `docker run -p 8081:80 --name team-page-container team-page`
3. `http://localhost:8081` im Browser pruefen

## Erweiterung

- Aendere den Text in `index.html`
- Baue das Image neu
- Starte den Container neu

## Aufraeumen

```bash
docker stop team-page-container
docker rm team-page-container
```
