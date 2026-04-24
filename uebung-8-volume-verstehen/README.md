# Uebung 8: Volume einbauen und verstehen

Ziel: Verstehen, warum ein benanntes Volume Daten ueber das Loeschen eines Containers hinaus erhalten kann.

## Dateien

- `compose.yaml`: startet Postgres mit benanntem Volume

## Schritte

1. `docker compose up -d`
2. `docker compose ps`
3. `docker volume ls`
4. `docker compose down`
5. `docker volume ls`

## Fragen

- Warum ist das Volume nach `docker compose down` noch vorhanden?
- Warum ist das bei Datenbanken wichtig?
- Was wuerde `docker compose down -v` zusaetzlich machen?

## Aufraeumen

```bash
docker compose down -v
```
