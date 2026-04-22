# Uebung 2: Container untersuchen

Ziel: Laufende Container anzeigen, stoppen, im Hintergrund starten und Logs lesen.

## Schritte

1. `docker run -d -p 8080:80 --name uebung2-nginx nginx`
2. `docker ps`
3. `docker logs uebung2-nginx`
4. `docker stop uebung2-nginx`
5. `docker start uebung2-nginx`
6. `docker ps`

## Zusatzaufgaben

- Finde die Container-ID mit `docker ps`.
- Erklaere, warum `-d` praktisch ist.
- Stoppe und entferne den Container am Ende.

## Aufraeumen

```bash
docker stop uebung2-nginx
docker rm uebung2-nginx
```
