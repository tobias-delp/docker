# Uebung 15: Kleine Kubernetes-Architektur lesen

Ziel: Deployment, Service und ConfigMap in einem kleinen Setup gemeinsam verstehen.

## Voraussetzung

Ein lokaler Kubernetes-Cluster ist optional. Die Uebung funktioniert auch als reine Lese- und Analyseaufgabe.

## Dateien

- `deployment.yaml`: App-Deployment mit einer Umgebungsvariable aus der ConfigMap
- `service.yaml`: stabiler Zugang zur App
- `configmap.yaml`: einfache Laufzeitkonfiguration

## Aufgaben

1. Lies alle drei Dateien.
2. Benenne, welche Rolle jede Ressource hat.
3. Erklaere, wie die App an ihre Konfiguration kommt.
4. Ueberlege, welche Ressource als Naechstes sinnvoll waere.

## Optional

```bash
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get all
```
