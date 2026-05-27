import tkinter as tk

def show_menu():
    menu_frame.pack(side="right", expand=True, fill="both")
    app_frame.pack_forget()

def show_calc():
    conv_frame.pack_forget()
    menu_frame.pack_forget()

    app_frame.pack()
    sidebar.pack(side="top",fill="x")
    content.pack(side="top", expand=True, fill="both")
    calc_frame.pack()

def show_conv():
    calc_frame.pack_forget()
    menu_frame.pack_forget()

    app_frame.pack()
    sidebar.pack(side="top")
    content.pack(side="bottom", expand=True, fill="both")
    conv_frame.pack()

root = tk.Tk()
root.title("FX-Converter Lab")
root.geometry("500x400") # Width x Length

menu_frame = tk.Frame(root)
app_frame = tk.Frame(root)

sidebar = tk.Frame(app_frame)
content = tk.Frame(app_frame)

conv_frame = tk.Frame(content)
calc_frame = tk.Frame(content)

menu_label = tk.Label(menu_frame, text="Menu", font=("Arial", 20))
calc_label = tk.Label(calc_frame, text="Calculator", font=("Arial", 20))
conv_label = tk.Label(conv_frame, text="Converter", font=("Arial", 20))

menu_label.pack(pady=20)
calc_label.pack(pady=20)
conv_label.pack(pady=20)

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

show_menu()

# Immer zum Ende - Tkiniter soll zuerst alle Elemente bekommen
def app():
    root.mainloop()


