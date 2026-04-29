# Uebung 18: Docker Build per Workflow verstehen

Ziel: Nachvollziehen, wie ein Workflow ein Docker Image baut.

## Dateien

- `.github/workflows/docker-build.yml`: Workflow fuer Docker Build
- `Dockerfile`: minimales Image
- `index.html`: statische Startseite

## Aufgaben

1. Oeffne Workflow und Dockerfile.
2. Finde den Step, der `docker build` ausfuehrt.
3. Erklaere, welche Dateien dafuer im Repository liegen muessen.
4. Benenne, was der Runner fuer den Build bereitstellt.
