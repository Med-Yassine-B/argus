import requests as req
import os
from dotenv import load_dotenv, find_dotenv

VALID_CURRENCY_CODES = {
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD",
    "CAD", "CDF", "CHF", "CLF", "CLP", "CNH", "CNY", "COP", "CRC", "CUP",
    "CVE", "CZK",
    "DJF", "DKK", "DOP", "DZD",
    "EGP", "ERN", "ETB", "EUR",
    "FJD", "FKP", "FOK",
    "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD",
    "HKD", "HNL", "HRK", "HTG", "HUF",
    "IDR", "ILS", "IMP", "INR", "IQD", "ISK",
    "JEP", "JMD", "JOD", "JPY",
    "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT",
    "LAK", "LBP", "LKR", "LRD", "LSL", "LYD",
    "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR",
    "MWK", "MXN", "MYR", "MZN",
    "NAD", "NGN", "NIO", "NOK", "NPR", "NZD",
    "OMR",
    "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG",
    "QAR",
    "RON", "RSD", "RUB", "RWF",
    "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SOS", "SRD",
    "SSP", "STN", "SYP", "SZL",
    "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS",
    "UAH", "UGX", "USD", "UYU", "UZS",
    "VES", "VND", "VUV",
    "WST",
    "XAF", "XCD", "XDR", "XOF", "XPF",
    "YER",
    "ZAR", "ZMW", "ZWL",
}

def check_currency(question):
    while True:
        resp = input(question)
        resp = resp.strip().upper()
        if resp in VALID_CURRENCY_CODES:
            return resp
        else:
            print("Ungültige Währung! Bitte erneut eingeben.")
            return None

def getResp(question):
    while True:
        resp = check_currency(question)
        if resp is not None:
            return resp

load_dotenv(find_dotenv())
api_key = os.getenv("api_key")

curr1 = ""
curr2 = ""


def getRates(curr1, curr2):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{curr1}/{curr2}"
    resp = req.get(url)
    data = resp.json()
    return data

# Testen, ob die API funktioniert
#data = getRates("EUR", "USD")
print("API funktioniert! Hier ein Beispiel für die Umrechnung von EUR zu USD:")