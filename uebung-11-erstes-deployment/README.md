# Uebung 11: Erstes Deployment anwenden

Ziel: Ein einfaches Deployment erstellen und die erzeugten Pods ansehen.

## Voraussetzung

Ein lokaler Kubernetes-Cluster ist verfuegbar, zum Beispiel ueber Docker Desktop, Minikube oder Kind.

## Dateien

- `deployment.yaml`: Deployment mit zwei nginx-Pods

## Schritte

1. `kubectl apply -f deployment.yaml`
2. `kubectl get deployments`
3. `kubectl get pods`

## Fragen

- Wie viele Pods wurden erstellt?
- Warum erzeugt das Deployment mehrere Pods?
- Welche Rolle spielt `replicas`?
