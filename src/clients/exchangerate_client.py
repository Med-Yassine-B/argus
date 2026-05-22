import requests as req
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
api_key = os.getenv("api_key")

data = {
    "result": "",
    "error-type": "",
    "conversion_rate": None
}

def get_rates(curr1, curr2):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{curr1}/{curr2}"
    try:
        resp = req.get(url, timeout=5)
        resp.raise_for_status()
        payload = resp.json()
        
    except req.exceptions.Timeout:
        print("API hat zu lange gebraucht.")
    except req.exceptions.ConnectionError:
        print("Keine Verbindung zur API.")
    except req.exceptions.RequestException as error:
        print(f"Request fehlgeschlagen: {error}")
    except ValueError:
        print("Fehler beim Verarbeiten der API-Antwort.")
    except KeyError:
        print("Unerwartete API-Antwortstruktur.")
    
    if payload.get("result") == "success":
        data["result"] = "success"
        data["conversion_rate"] = payload.get("conversion_rate")
        return data
    else:
        data["result"] = "error"
        data["error_type"] = payload.get("error-type")
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