# Uebung 4: Dockerfile lesen und verbessern

Ziel: Ein einfaches Python-Beispiel analysieren und danach verbessern.

## Dateien

- `app.py`: kleine Flask-Anwendung
- `Dockerfile`: absichtlich einfach gehalten
- `requirements.txt`: Python-Abhaengigkeiten
- `.dockerignore`: vermeidet unnoetige Dateien im Build-Kontext

## Schritte

1. Dockerfile lesen und erklaeren
2. `docker build -t flask-demo .`
3. `docker run -p 5000:5000 --name flask-demo-container flask-demo`
4. `http://localhost:5000` im Browser pruefen

## Diskussionspunkte

- Warum ist `COPY requirements.txt ./` vor `COPY . .` oft besser?
- Warum ist `.dockerignore` sinnvoll?
- Was passiert, wenn der Port im Container nicht veroeffentlicht wird?
