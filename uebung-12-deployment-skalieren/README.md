# Uebung 12: Deployment skalieren

Ziel: Ein Deployment anwenden und die Anzahl der laufenden Pods erhoehen.

## Voraussetzung

Ein lokaler Kubernetes-Cluster ist verfuegbar.

## Dateien

- `deployment.yaml`: Deployment mit einer Replik

## Schritte

1. `kubectl apply -f deployment.yaml`
2. `kubectl get deployments`
3. `kubectl scale deployment webapp --replicas=3`
4. `kubectl get pods`

## Fragen

- Wie viele Pods liefen vorher?
- Wie viele Pods laufen nach dem Skalieren?
- Wann ist horizontale Skalierung sinnvoll?
