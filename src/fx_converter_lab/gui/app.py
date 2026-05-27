import tkinter as tk

root = tk.Tk()
root.title("FX-Converter Lab")
root.geometry("500x400") # Width x Length

content = tk.Frame(root)
content.pack(side="right", expand=True, fill="both")

menu_frame = tk.Frame(content)
conv_frame = tk.Frame(content)
calc_frame = tk.Frame(content)

sidebar_calc = tk.Frame(calc_frame,width=160, bg="lightgray")
sidebar_calc.pack(side="top", fill="y")
sidebar_conv = tk.Frame(conv_frame,width=160, bg="lightgray")
sidebar_conv.pack(side="top", fill="y")

for frame in (menu_frame, calc_frame, conv_frame):
    frame.grid(row=0, column=0, sticky="nsew")

content.grid_rowconfigure(0, weight=1)
content.grid_columnconfigure(0, weight=1)

def show_frame(Frame):
    Frame.tkraise()

tk.Label(menu_frame, text="Menu", font=("Arial", 20)).pack(pady=20)
tk.Label(calc_frame, text="Calculator", font=("Arial", 20)).pack(pady=20)
tk.Label(conv_frame, text="Converter", font=("Arial", 20)).pack(pady=20)

button_conv = tk.Button(menu_frame, text="Converter",command=lambda: show_frame(conv_frame)).pack(fill="x", padx=10, pady=10)
button_calc = tk.Button(menu_frame, text="Calculator",command=lambda: show_frame(calc_frame)).pack(fill="x", padx=10, pady=10)

show_frame(menu_frame)

# Immer zum Ende - Tkiniter soll zuerst alle Elemente bekommen
root.mainloop()


