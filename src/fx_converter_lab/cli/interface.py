from fx_converter_lab.services.calculator_service import check_num,check_op,calc
from fx_converter_lab.services.conversion_service import convert,check_currency


def display_convert() -> None:
    while True:
        amount = check_num(input("Amount: "))
        if amount is None:
            print("Please enter a valid amount in the 'Amount' field.")
            continue
        break
    while True:
        resp1 = check_currency(input("First currency: "))
        if resp1 is None:
            print("Unvalid currency! Please enter again.")
            continue
        break
    while True:
        resp2 = check_currency(input("Second currency: "))
        if resp2 is None:
            print("Unvalid currency! Please enter again..")
            continue
        break
    while True:
        response = convert(amount,resp1,resp2)
        if response is None:
            print("Error with the API request! Please try again later.")
            continue
        break
        
    result = response
    print (f"The exchange rate from {resp1} to {resp2} for {amount} {resp1} is {result} {resp2}")
        
    if return_to_menu() == 'y':
        return

def display_calc() -> None:
    while True:
        num1 = check_num(input("First number: "))
        if num1 is None:
            print("Please enter again!")
            continue
        break
    while True:
        num2 = check_num(input("Second number: "))
        if num2 is None:
            print("Please enter again!")
            continue
        break
    while True:
        op = input("Which operation do you wanna apply? (+,-,*,/,%,**) ")
        if check_op(op) is False:
            print("Please enter again!")
            continue
        break
        
    result = calc(num1,num2,op)
    print(f"Berechnung: {num1} {op} {num2} = {result}")
        
    if return_to_menu() == 'y':
        return

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