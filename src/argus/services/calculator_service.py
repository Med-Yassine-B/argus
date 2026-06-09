from argus.domain.validation import is_valid_op

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