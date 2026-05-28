from fx_converter_lab.services.calculator_service import get_num,get_op,calc
from fx_converter_lab.services.conversion_service import convert,check_currency


def display_convert() -> None:
    while True:
        amount = get_num()
        resp1 = check_currency(input("Which first currency would you like?"))
        if resp1 is None:
            print("Unvalid currency! Please enter again.")
            continue
        resp2 = check_currency(input("Which second currency would you like??"))
        if resp1 is None:
            print("Unvalid currency! Please enter again..")
            continue
        response = convert(amount,resp1,resp2)
        if response is None:
            print("Error with the API request! Please try again later.")
            continue
        
        result = response
        print (f"The exchange rate from {resp1} to {resp2} for {amount} {resp1} is {result} {resp2}")
            

        if return_to_menu() == 'y':
            break

def display_calc() -> None:
    num1 = 0
    num2 = 0
    while True:
        num1 = get_num()
        num2 = get_num()
        op = get_op()
        result = calc(num1,num2,op)
        print(f"Berechnung: {num1} {op} {num2} = {result}")
        
        if return_to_menu() == 'y':
            break

def return_to_menu() -> str:
    while True:
        repeat = input("Would you like to return to the menu? (y/n) ")
        match repeat:
            case 'y':
                return 'y'
            case 'n':
                return 'n'
            case _:
                print("Please enter 'y' or 'n'!")

def dev_interface() -> None:
    initConv = "Welcome to the Calculator with Currency Conversion!"
    print(initConv)
    while True:
        print("Menu: \n(1) Calculator \n(2) Exchnage Rate \n(3) Exit")
        option = input("Please select an option: ")
        match option:
            case '1':
                display_calc()
            case '2':
                display_convert()
            case '3':
                break
            case _:
                print("Please enter only '1','2' or '3'!")