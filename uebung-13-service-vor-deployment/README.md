# Uebung 13: Service vor ein Deployment setzen

Ziel: Verstehen, wie ein Service Pods ueber Labels findet und stabil erreichbar macht.

## Voraussetzung

Ein lokaler Kubernetes-Cluster ist verfuegbar.

## Dateien

- `deployment.yaml`: Deployment mit zwei Web-Pods
- `service.yaml`: ClusterIP-Service fuer das Deployment

## Schritte

1. `kubectl apply -f deployment.yaml`
2. `kubectl apply -f service.yaml`
3. `kubectl get pods`
4. `kubectl get svc`
5. `kubectl port-forward svc/webapp-service 8080:80`

## Fragen

- Welche Labels tragen die Pods?
- Welchen Selector nutzt der Service?
- Warum ist der Service stabil, obwohl Pods ersetzt werden koennen?
