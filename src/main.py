from clients import exchangerate_client as api

def getNum():
    # Tipp: Bool-Werte müssen nicht in Klammern stehen
    while True:
        try:
            num = float(input("Gib die Zahl ein:"))
            return num 
        except ValueError:
            print("Bitte eine Zahl eingeben!!")

def getOperator():
    # Tipp: Liste verwenden, wenn mehr als 2 Optionen für etwas besteht
    valid_ops = ['+', '-', '*', '/', '%', '**']
    while True:
        op = input("Welche Rechenoperation wollen Sie anwenden? (+,-,*,/,%,**) ")
        if op in valid_ops:
            return op
        else:
            print("Bitte erneut eingeben!")

def getCurr():
    while True:
        resp1 = api.getResp("Welche erste Währung wollen Sie?")
        resp2 = api.getResp("Welche zweite Währung wollen Sie?")

        data = api.getRates(resp1, resp2)

        match data['result']:
            case 'success':
                return data['conversion_rate'], resp1, resp2
            case 'error':
                check_error(data['error-type'])

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
      
def convert(amount):
    data = getCurr()
    if data is not None:
        return amount * data[0], data[1], data[2]
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

def displayConvert():
    while True:
        amount = getNum()
        result, resp1, resp2 = convert(amount)

        if result is not None:
            print (f"Der Wechselkurs von {resp1} zu {resp2} mit {amount} {resp1} ergibt {result} {resp2}")

        while True:
            repeat = input("Wollen Sie eine neue Berechnung ausführen? (y/n) ")
            match repeat:
                case 'y':
                    break
                case 'n':
                    return
                case _:
                    print("Bitte 'y' oder 'n' eingeben!")

def displayCalc():
    num1 = 0
    num2 = 0
    while True:
        # Tipp: Man muss nicht die Variable weiterreichen, die zum Speichern des Return-Values da ist
        num1 = getNum()
        num2 = getNum()
        op = getOperator()
        result = calc(num1,num2,op)
        print(f"Berechnung: {num1} {op} {num2} = {result}")
        while True:
            repeat = input("Wollen Sie eine neue Berechnung ausführen? (y/n) ")
            match repeat:
                case 'y':
                    break
                case 'n':
                    return
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
                displayCalc()
            case '2':
                displayConvert()
            case '3':
                break
            case _:
                print("Bitte nur '1','2' oder '3' eingeben!")

main()

    