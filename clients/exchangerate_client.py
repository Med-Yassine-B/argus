import requests as req
import os
from dotenv import load_dotenv, find_dotenv

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
# print(data)