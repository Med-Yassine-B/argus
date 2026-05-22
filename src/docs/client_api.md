# ExchangeRate-Client

Kurzbeschreibung

Der ExchangeRate-Client ist in `src/clients/exchangerate_client.py` implementiert und stellt die Funktion `get_rates(curr1, curr2)` zur Verfügung. Die Funktion ruft die API von exchangerate-api.com ab und verwendet den API-Key aus der `.env`-Datei (Umgebungsvariable `api_key`).

Rückgabe

- Bei Erfolg: Ein Dictionary mit mindestens `{ "result": "success", "conversion_rate": <float> }`.
- Bei Fehlern: `None` (zusätzlich werden deutsche Fehlermeldungen auf STDOUT ausgegeben).

Fehler- und Timeout-Verhalten

- Timeout: 5 Sekunden; die Implementierung fängt `Timeout`, `ConnectionError`, `RequestException`, `ValueError` und `KeyError` ab und gibt bei Bedarf Hinweise auf der Konsole aus.
- API-spezifische Fehler (`unsupported-code`, `malformed-request`, `invalid-key`, `inactive-account`, `quota-reached`) werden von `check_error(err_type)` verarbeitet und als aussagekräftige deutsche Meldungen ausgegeben.

Integration

In `src/main.py` wird der Client wie folgt eingebunden: `from clients import exchangerate_client as api` und über `api.get_rates()` in den Funktionen `get_conv_rate()` / `convert()` verwendet, um Wechselkurse für Benutzereingaben zu ermitteln.

Beispiel

```py
# Beispielaufruf
data = get_rates("EUR", "USD")
if data is not None and data.get("result") == "success":
	rate = data["conversion_rate"]
	# weiterverarbeiten
else:
	# Fehlerbehandlung (siehe Konsolenausgaben)
```

Hinweis: Der Client liefert ein vereinfachtes, rohes Dictionary zurück; die Aufbereitung für Anzeige oder weitere Logik erfolgt in der aufrufenden Anwendung.
