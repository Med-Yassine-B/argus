def checkOp(num1,num2,op):
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
            # Tipp: Für undefinierte Zustände einfach 'None' zurückgeben
            return None
        
def getNum():
    # Tipp: Bool-Werte müssen nicht in Klammern stehen
    while True:
        try:
            num = float(input("Gib die Zahl ein:"))
            return num 
        except ValueError:
            print("Bitte eine Zahl eingeben!!")
    
def main():
    initConv = "Willkommen zum Basic Calculator!"
    num1 = 0
    num2 = 0
    print(initConv)
    while True:
        # Tipp: Man muss nicht die Variable weiterreichen, die zum Speichern des Return-Values da ist
        num1 = getNum()
        num2 = getNum()

        while(True):
            op = input("Welche Rechenoperation wollen Sie anwenden? (+,-,*,/,%,**) ")
            result = checkOp(num1,num2,op)

            if result is None:
                print("Bitte erneut eingeben!")
            else:
                break

        print(result)
        while True:
            repeat = input("Wollen Sie eine neue Berechnung ausführen? (y/n) ")
            match repeat:
                case 'y':
                    break
                case 'n':
                    return
                case _:
                    print("Bitte 'y' oder 'n' eingeben!")
main()

    