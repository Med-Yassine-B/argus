initConv = "Willkommen zum Basic Calculator!"
err = "Falsche Eingabe!"

def checkOp(num1,num2,op):
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
        

    

print(initConv) 

while(True):
    try:
        num1 = int(input("Gib die erste Zahl ein:"))
        break
    except ValueError:
        print("Bitte eine Zahl eingeben!!")

while(True):
    try:
        num2 = int(input("Gib die zweite Zahl ein:"))
        break
    except ValueError:
        print("Bitte eine Zahl eingeben!!")

while(True):
    op = input("Welche Rechenoperation wollen Sie anwenden? (+,-,*,/,%,**) ")
    result = checkOp(num1,num2,op)

    if result is None:
        print("Bitte erneut eingeben!")
    else:
        break

print(result)