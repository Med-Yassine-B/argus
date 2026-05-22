from clients import exchangerate_client as api

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

def get_num():
    # Tipp: Bool-Werte müssen nicht in Klammern stehen
    while True:
        try:
            num = float(input("Gib die Zahl ein:"))
            return num 
        except ValueError:
            print("Bitte eine Zahl eingeben!!")

def get_operator():
    # Tipp: Liste verwenden, wenn mehr als 2 Optionen für etwas besteht
    valid_ops = ['+', '-', '*', '/', '%', '**']
    while True:
        op = input("Welche Rechenoperation wollen Sie anwenden? (+,-,*,/,%,**) ")
        if op in valid_ops:
            return op
        else:
            print("Bitte erneut eingeben!")

def check_currency(question):
    while True:
        resp = input(question)
        resp = resp.strip().upper()
        if resp in VALID_CURRENCY_CODES:
            return resp
        else:
            print("Ungültige Währung! Bitte erneut eingeben.")
            # return None

"""
def get_resp(question):
    while True:
        resp = check_currency(question)
        if resp is not None:
            return resp
"""

def get_conv_rate():
    while True:
        resp1 = check_currency("Welche erste Währung wollen Sie?")
        resp2 = check_currency("Welche zweite Währung wollen Sie?")

        data = api.get_rates(resp1, resp2)
        if data is not None:
            return {
                "rate": data["conversion_rate"],
                "from": resp1,
                "to": resp2
            }
        else:
            return None

def convert(amount):
    data = get_conv_rate()
    if data is not None:
        return amount * data["rate"], data["from"], data["to"]
    else:
        return None


def calc(num1,num2,op):
        # Tipp: Auf Ifelse verzichten, wenn davon mehr als 3 Stück entstehen
        match op:
            case '+':
                return num1 + num2
            case '-': 
                return num1 - num2
            case '*': 
                return num1 * num2
            case '/': 
                try:
                    return num1 / num2
                except ZeroDivisionError:
                    print("Divison durch null nicht möglich!")
                    return None
            case '%': 
                return num1 % num2
            case '**': 
                return num1 ** num2
            case _:
                return None

def display_convert():
    while True:
        amount = get_num()
        result, resp1, resp2 = convert(amount)

        if result is not None:
            print (f"Der Wechselkurs von {resp1} zu {resp2} mit {amount} {resp1} ergibt {result} {resp2}")
        else:
            print("Fehler bei der API-Anfrage! Bitte später erneut versuchen.")

        if return_to_menu() == 'y':
            break

def display_calc():
    num1 = 0
    num2 = 0
    while True:
        # Tipp: Man muss nicht die Variable weiterreichen, die zum Speichern des Return-Values da ist
        num1 = get_num()
        num2 = get_num()
        op = get_operator()
        result = calc(num1,num2,op)
        print(f"Berechnung: {num1} {op} {num2} = {result}")

    return_to_menu()

def return_to_menu():
    while True:
        repeat = input("Wollen Sie zum Menü zurückkehren? (y/n) ")
        match repeat:
            case 'y':
                return 'y'
            case 'n':
                return 'n'
            case _:
                print("Bitte 'y' oder 'n' eingeben!")

def main():
    initConv = "Willkommen zum Calculator mit Wechselkurberechnung!"
    print(initConv)
    while True:
        print("Menü: \n(1) Calculator \n(2) Exchnage Rate \n(3) Exit")
        option = input("Wählen Sie bitte eine Option aus ")
        match option:
            case '1':
                display_calc()
            case '2':
                display_convert()
            case '3':
                break
            case _:
                print("Bitte nur '1','2' oder '3' eingeben!")

main()

    