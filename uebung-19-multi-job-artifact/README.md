# Uebung 19: Multi-Job Pipeline mit Artifact lesen

Ziel: Verstehen, wie ein Job eine Datei erzeugt und ein anderer Job sie weiterverwendet.

## Dateien

- `.github/workflows/multi-job.yml`: Workflow mit Build- und Test-Job
- `message.txt`: Eingabedatei fuer den Build-Schritt

## Aufgaben

1. Oeffne den Workflow.
2. Finde den Build-Job und den Test-Job.
3. Benenne das Artifact.
4. Erklaere, warum `needs: build` wichtig ist.
