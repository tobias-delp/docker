# Uebung 1: Ersten Container starten

Ziel: Einen fertigen Container starten und den Unterschied zwischen Image und Container verstehen.

## Schritte

1. `docker run hello-world`
2. `docker run -p 8080:80 --name uebung1-nginx nginx`
3. `http://localhost:8080` im Browser oeffnen

## Leitfragen

- Welches Image wurde heruntergeladen?
- Welcher Container laeuft danach lokal?
- Was ist der Unterschied zwischen Image und Container?

## Aufraeumen

```bash
docker stop uebung1-nginx
docker rm uebung1-nginx
```
