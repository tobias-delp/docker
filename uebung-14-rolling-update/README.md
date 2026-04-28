# Uebung 14: Rolling Update beobachten

Ziel: Ein Deployment zuerst mit Version 1 und danach mit Version 2 ausrollen.

## Voraussetzung

Ein lokaler Kubernetes-Cluster ist verfuegbar.

## Dateien

- `deployment-v1.yaml`: Deployment mit `nginx:1.25`
- `deployment-v2.yaml`: Deployment mit `nginx:1.27`

## Schritte

1. `kubectl apply -f deployment-v1.yaml`
2. `kubectl get pods`
3. `kubectl apply -f deployment-v2.yaml`
4. `kubectl rollout status deployment/webapp`
5. `kubectl describe deployment webapp`

## Fragen

- Was aendert sich zwischen den beiden Manifests?
- Warum muessen nicht alle Pods gleichzeitig ersetzt werden?
- Welche Idee steckt hinter einem Rolling Update?
