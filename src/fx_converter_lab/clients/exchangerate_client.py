import requests as req
from fx_converter_lab.config import (EXCHANGE_RATE_BASE_URL ,EXCHANGE_RATE_API_KEY,REQUEST_TIMEOUT_SECONDS)

def get_rates(curr1, curr2):
    url = f"{EXCHANGE_RATE_BASE_URL}/{EXCHANGE_RATE_API_KEY}/pair/{curr1}/{curr2}"
    data = {
        "result": "",
        "error_type": "",
        "conversion_rate": None
    }
    
    try:
        resp = req.get(url, timeout=REQUEST_TIMEOUT_SECONDS)
        resp.raise_for_status()
        payload = resp.json()
        
    except req.exceptions.Timeout:
        print("API hat zu lange gebraucht.")
        return None
    except req.exceptions.ConnectionError:
        print("Keine Verbindung zur API.")
        return None
    except req.exceptions.RequestException as error:
        print(f"Request fehlgeschlagen: {error}")
        # Request fehlgeschlagen: 403 Client Error: Forbidden for url: https://v6.exchangerate-api.com/v6/None/pair/EUR/USD -> sollte nicht gezeigt werden!!!
        return None
    except ValueError:
        print("Fehler beim Verarbeiten der API-Antwort.")
        return None
    except KeyError:
        print("Unerwartete API-Antwortstruktur.")
        return None
    
    if payload.get("result") == "success":
        data["result"] = "success"
        data["conversion_rate"] = payload.get("conversion_rate")
        return data
    else:
        data["result"] = "error"
        data["error_type"] = payload.get("error_type")
        check_error(data["error_type"])
        return None
 

def check_error(err_type):
    match err_type:
        case 'unsupported-code' | 'malformed-request':
            print("Ungültige Anfrage! Bitter versuchen Sie es später erneut.")
        case 'invalid-key':
            print("Ungültiger API-Key! Checken Sie Ihren API-Key und versuchen Sie es erneut.")
        case 'inactive-account':
            print("Inaktives Konto! Bitte auf exchangerate-api.com gehen und Konto aktivieren.")
        case 'quota-reached':
            print("Anfrage-Limit erreicht! Bitte später erneut versuchen oder auf exchangerate-api.com upgraden.")

# Testen, ob die API funktioniert
#data = get_rates("EUR", "USD")