import requests as req

url = "https://v6.exchangerate-api.com/v6/8ef8d96608f75de7f8788b7a/latest/USD"

resp = req.get(url)
data = resp.json()

# print(data["conversion_rates"]["EUR"])