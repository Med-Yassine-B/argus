from fx_converter_lab.clients import exchangerate_client as ex_client
from fx_converter_lab.domain.currency import normalize_input_string,is_valid_curr_code



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
        resp = normalize_input_string(input(question))

        if is_valid_curr_code:
            return resp
        
        print("Ungültige Währung! Bitte erneut eingeben.")


def get_conv_rate():
    resp1 = check_currency("Welche erste Währung wollen Sie?")
    resp2 = check_currency("Welche zweite Währung wollen Sie?")

    data = ex_client.get_rates(resp1, resp2)
        
    if data is None:
        return None
        
    return {
        "rate": data["conversion_rate"],
        "from": resp1,
        "to": resp2
    }

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
            print (f"Der Wechselkurs von {resp1} zu {resp2} mit {amount} {resp1} ergibt {result:,.2f} {resp2}")
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

    