import api_test as api

def getRates():
    data = api.data["conversion_rates"]
    return data 

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
    data = getRates()
    while True:
        resp = input("Welche Währung wollen Sie?")
        if resp in data:
            return resp
        else:
            print("Bitt eine gültige Währung eingeben")
      
def convert():
    data = getRates()


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
        # Tipp: Man muss nicht die Variable weiterreichen, die zum Speichern des Return-Values da ist
        amount = getNum()
        from_curr = getCurr()
        to_curr = getCurr()
        result = convert(amount,from_curr,to_curr)
        print(f"Wechelkurs von {from_curr} zu {to_curr} mit {amount} {from_curr} ergibt {result}")
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
        option = input("Wählen Sie bitte eine Option aus")
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

    