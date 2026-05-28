import tkinter as tk
from fx_converter_lab.services.calculator_service import calc, check_num, check_op
from fx_converter_lab.services.conversion_service import convert,check_currency

def show_menu():
    menu_frame.pack(side="right", expand=True, fill="both")
    app_frame.pack_forget()
    num1.delete("0",tk.END)
    num2.delete("0",tk.END)
    op_e.delete("0",tk.END)
    curr1.delete("0",tk.END)
    curr2.delete("0",tk.END)
    amount_e.delete("0",tk.END)

def show_calc():
    conv_frame.grid_forget()
    menu_frame.pack_forget()
    num1.delete("0",tk.END)
    num2.delete("0",tk.END)
    op_e.delete("0",tk.END)
    curr1.delete("0",tk.END)
    curr2.delete("0",tk.END)
    amount_e.delete("0",tk.END)

    app_frame.pack()
    sidebar.pack(side="top",fill="x")
    content.pack(side="top", expand=True, fill="both")
    calc_frame.grid()

def show_conv():
    calc_frame.grid_forget()
    menu_frame.pack_forget()
    num1.delete("0",tk.END)
    num2.delete("0",tk.END)
    op_e.delete("0",tk.END)
    curr1.delete("0",tk.END)
    curr2.delete("0",tk.END)
    amount_e.delete("0",tk.END)

    app_frame.pack()
    sidebar.pack(side="top")
    content.pack(side="bottom", expand=True, fill="both")
    conv_frame.grid()

def act_calculate():
    resp1 = num1.get()
    resp1 = check_num(resp1)
    resp2 = num2.get()
    resp2 = check_num(resp2)
    op = op_e.get()
    if resp1 is None:
        result_label.config(text="Bitte eine gültige Zahl für 'Number 1' eingeben")
        return 
    if resp2 is None:
        result_label.config(text="Bitte eine gültige Zahl für 'Number 2' eingeben")     
        return
    if check_op(op) is False:
        result_label.config(text="Bitte eine gültige Operation für 'Operation' eingeben")  
        return
    result = calc(resp1,resp2,op)
    if result is None:
        result_label.config(text="Division durch 0 nicht möglich")  
        return
    result_label.config(text=f"{resp1} {op} {resp2} = {result}")

def act_convert():
    resp1 = check_currency(curr1.get())
    resp2 = check_currency(curr2.get())
    amount = check_num(amount_e.get())
    if resp1 is None:
        result_label.config(text="Bitte eine gültige Währung für 'Currency 1' eingeben")
        return 
    if resp2 is None:
        result_label.config(text="Bitte eine gültige Währung für 'Currency 2' eingeben")
        return 
    if resp2 is None:
        result_label.config(text="Bitte eine gültige Menge für 'Amount' eingeben")     
        return
    result = convert(amount,resp1,resp2)
    result_label.config(text=f"Der Wechselkurs von {resp1} zu {resp2} mit {amount} {resp1} ergibt {result:,.2f} {resp2}")
    

# Window
root = tk.Tk()
root.title("FX-Converter Lab")
root.geometry("500x400") # Width x Length

# Frames
menu_frame = tk.Frame(root)
app_frame = tk.Frame(root)

sidebar = tk.Frame(app_frame)
content = tk.Frame(app_frame)

conv_frame = tk.Frame(content)
calc_frame = tk.Frame(content)

# Labels
menu_label = tk.Label(menu_frame, text="Menu", font=("Arial", 20))
calc_label = tk.Label(calc_frame, text="Calculator", font=("Arial", 20))
conv_label = tk.Label(conv_frame, text="Converter", font=("Arial", 20))

num1_label = tk.Label(calc_frame, text="Number 1:")
num2_label = tk.Label(calc_frame, text="Number 2:")
op_label = tk.Label(calc_frame, text="Operation:")
result_label = tk.Label(calc_frame)

menu_label.pack(pady=20)
calc_label.grid(pady=20,column=1,row=0)
conv_label.grid(pady=20,column=1,row=0)

num1_label.grid(pady=5,column=0,row=1)
num2_label.grid(pady=5,column=0,row=2)
op_label.grid(pady=5,column=0,row=3)
result_label.grid(column=1,row=5)

# Entries
num1 = tk.Entry(calc_frame)
num2 = tk.Entry(calc_frame)
op_e = tk.Entry(calc_frame)

num1.grid(pady=5,column=1,row=1)
num2.grid(pady=5,column=1,row=2)
op_e.grid(pady=5,column=1,row=3)

num1.focus()

amount_e = tk.Entry(conv_frame)
curr1 = tk.Entry(conv_frame)
curr2 = tk.Entry(conv_frame)

amount_e.grid(pady=5,column=1,row=1)
num1.grid(pady=5,column=1,row=2)
num2.grid(pady=5,column=1,row=3)

amount_e.focus()

# Buttons

from_menu_calc = tk.Button(menu_frame, text="Calculator",command=show_calc)
from_menu_conv = tk.Button(menu_frame, text="Converter",command=show_conv)

from_menu_calc.pack(fill="x", padx=100, pady=10)
from_menu_conv.pack(fill="x", padx=100, pady=10)

from_sidebar_calc = tk.Button(sidebar, text="Calculator",command=show_calc)
from_sidebar_conv = tk.Button(sidebar, text="Converter",command=show_conv)
return_menu = tk.Button(sidebar, text="Back to menu",command=show_menu)

from_sidebar_calc.pack(side="left")
from_sidebar_conv.pack(side="left")
return_menu.pack(side="left")

click_calculate = tk.Button(calc_frame, text="Calculate",command=act_calculate)
click_calculate.grid(column=1,row=4)

click_converter = tk.Button(conv_frame, text="Calculate",command=act_calculate)
click_converter.grid(column=1,row=4)
show_menu()

# Immer zum Ende - Tkiniter soll zuerst alle Elemente bekommen
def app():
    root.mainloop()


