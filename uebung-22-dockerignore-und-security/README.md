# Uebung 22: .dockerignore und Security

Ziel: Verstehen, welche Dateien nicht in den Build-Kontext gehoeren und warum ein Container nicht als root laufen sollte.

## Dateien

- `Dockerfile`: Beispiel mit Nicht-Root-User
- `.dockerignore`: ausgeschlossene Dateien
- `.env`: absichtlich vorhandene Datei fuer die Diskussion
- `index.js`: kleines Beispiel

## Aufgaben

1. Lies `.dockerignore` und benenne die ausgeschlossenen Dateien.
2. Erklaere, warum `.env` und `.git` nicht ins Image gehoeren.
3. Finde die Stelle im Dockerfile, an der ein Nicht-Root-User verwendet wird.
