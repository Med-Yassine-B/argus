from fx_converter_lab.service.conversion_service import convert
from fx_converter_lab.service.calculator_service import get_num,get_op,calc


def display_convert() -> None:
    while True:
        amount = get_num()
        response = convert(amount)

        if response is not None:
            result, resp1, resp2 = response
            print (f"Der Wechselkurs von {resp1} zu {resp2} mit {amount} {resp1} ergibt {result:,.2f} {resp2}")
        else:
            print("Fehler bei der API-Anfrage! Bitte später erneut versuchen.")

        if return_to_menu() == 'y':
            break

def display_calc() -> None:
    num1 = 0
    num2 = 0
    while True:
        # Tipp: Man muss nicht die Variable weiterreichen, die zum Speichern des Return-Values da ist
        num1 = get_num()
        num2 = get_num()
        op = get_op()
        result = calc(num1,num2,op)
        print(f"Berechnung: {num1} {op} {num2} = {result}")
        
        if return_to_menu() == 'y':
            break

def return_to_menu() -> str:
    while True:
        repeat = input("Wollen Sie zum Menü zurückkehren? (y/n) ")
        match repeat:
            case 'y':
                return 'y'
            case 'n':
                return 'n'
            case _:
                print("Bitte 'y' oder 'n' eingeben!")

def dev_interface() -> None:
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