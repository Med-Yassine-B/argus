import tkinter as tk

def show_menu():
    menu_frame.pack(side="right", expand=True, fill="both")
    app_frame.pack_forget()

def show_calc():
    conv_frame.grid_forget()
    menu_frame.pack_forget()

    app_frame.pack()
    sidebar.pack(side="top",fill="x")
    content.pack(side="top", expand=True, fill="both")
    calc_frame.grid()

def show_conv():
    calc_frame.grid_forget()
    menu_frame.pack_forget()

    app_frame.pack()
    sidebar.pack(side="top")
    content.pack(side="bottom", expand=True, fill="both")
    conv_frame.grid()

def act_calculate():
    result_label.config(text="Button clicked")

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
op = tk.Entry(calc_frame)

num1.grid(pady=5,column=1,row=1)
num2.grid(pady=5,column=1,row=2)
op.grid(pady=5,column=1,row=3)

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

show_menu()

# Immer zum Ende - Tkiniter soll zuerst alle Elemente bekommen
def app():
    root.mainloop()


