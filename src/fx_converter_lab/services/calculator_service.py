from fx_converter_lab.domain.convert_valid import is_valid_op

def get_num() -> float | None:
    # Tipp: Bool-Werte müssen nicht in Klammern stehen
    while True:
        try:
            num = float(input("Gib die Zahl ein:"))
            return num 
        except ValueError:
            print("Bitte eine Zahl eingeben!")

def check_num(value:str) -> float | None:
    while True:
        try:
            num = float(value)
            return num
        except ValueError:
            return None

def get_op() -> str | None:
    # Tipp: Liste verwenden, wenn mehr als 2 Optionen für etwas besteht
    while True:
        op = input("Welche Rechenoperation wollen Sie anwenden? (+,-,*,/,%,**) ")
        if is_valid_op(op):
            return op
        else:
            print("Bitte erneut eingeben!")

def check_op(op:str) -> bool:
    # Tipp: Liste verwenden, wenn mehr als 2 Optionen für etwas besteht
    if is_valid_op(op):
        return True
    else:
        return False


def calc(num1:float,num2:float,op:str) -> float | None:
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
                    return None
            case '%': 
                return num1 % num2
            case '**': 
                return num1 ** num2
            case _:
                return None