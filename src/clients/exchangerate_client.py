import requests as req
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
api_key = os.getenv("api_key")

dict data = {
    "result": "",
    "error-type": ""
    "conversion_rate": 0.0
}

def get_rates(curr1, curr2):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{curr1}/{curr2}"
    try:
        resp = req.get(url, timeout=5)
        resp = resp.json()
        data['result'], data['conversion_rate'], data['error-type'] = resp['result'], resp['conversion_rate'], resp['error-type']
    except requests.exceptions.Timeout:
        print("API hat zu lange gebraucht.")
    except requests.exceptions.ConnectionError:
        print("Keine Verbindung zur API.")
    except requests.exceptions.RequestException as error:
        print(f"Request fehlgeschlagen: {error}")
    except ValueError:
        print("Fehler beim Verarbeiten der API-Antwort.")
    except KeyError:
        print("Unerwartete API-Antwortstruktur.")
    except data['result'] == 'error':
        check_error(data['error-type'])
    
    return data
 

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