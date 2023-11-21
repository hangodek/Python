import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import numpy as np
from matplotlib import pyplot
import math
import random
import sys


# Matplotlib

def matplotlib_windows():

    def adder():
        value_1 = entry_year.get()
        value_2 = entry_value.get()

        if value_1 and value_2 is not None:
            entry_listbox.insert(tk.END, f"Year : {value_1} Value : {value_2}")
            entry_year.delete(0, tk.END)
            entry_value.delete(0, tk.END)
        else:
            messagebox.showwarning("Error when inputing", "Please input the correct value")

    def submitter():
        temporary = entry_listbox.get(0, tk.END)
        
        temporary_value_1 = []
        temporary_value_2 = []

        for i in temporary:
            temporary_data = i.split("Value :")
            temporary_year = float(temporary_data[0].split("Year : ")[1])
            temporary_value = float(temporary_data[1])
            temporary_value_1.append(temporary_year)
            temporary_value_2.append(temporary_value)
            
        
        storage = "\n".join(temporary)
        messagebox.showinfo("Submitted Value", f"You has been submitted value : \n\n{storage}")
        asker = messagebox.askyesno("Convert to graphic", "Do you want to convert the value to matplot graphic ?")
        if asker:
            root.destroy()
            title = simpledialog.askstring("Graphic title", "Please enter the title for graphic plot")

            year = np.array(temporary_value_1)
            value = np.array(temporary_value_2)

            pyplot.plot(year, value, "o-r")
            pyplot.title(title.title())
            pyplot.xlabel("Years")
            pyplot.ylabel("Growth")
            pyplot.grid(axis = "both")
            pyplot.show()
        else:
            root.destroy()

   
    root = tk.Tk()
    root.title("Matplotlib Graphic Automation")
    root.geometry("400x400")
    frame = tk.Frame(root)
    frame.pack()
    label_year = tk.Label(frame, text = "Year :")
    label_year.grid(row = 0, column = 0, padx = 10, pady = 5)
    entry_year = tk.Entry(frame, width = 30)
    entry_year.grid(row = 0, column = 1, padx = 10, pady = 5)
    label_value = tk.Label(frame, text = "Value :")
    label_value.grid(row = 1, column = 0, padx = 10, pady = 5)
    entry_value = tk.Entry(frame, width = 30)
    entry_value.grid(row = 1, column = 1, padx = 10, pady= 5)
    add_value = tk.Button(frame, text = "Add", command = adder)
    add_value.grid(row = 2, columnspan = 2, padx= 10, pady = 10)
    entry_listbox = tk.Listbox(frame, width = 60, height = 10)
    entry_listbox.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
    submit_value = tk.Button(frame, text = "Submit", command = submitter)
    submit_value.grid(row = 4, columnspan = 2, padx = 10, pady= 10)
    #root.bind("<Configure>", windows_resizer)



# Rgb root system
def rgb_window():
    root = tk.Toplevel()
    frame = tk.Frame(root)
    frame.pack()
    random_text_generator_button = tk.Button(frame, text = "Random text generator", command = rgb_windows_random_text_generator)
    random_text_generator_button.pack()

def rgb_windows_random_text_generator():

    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"#{r:02x}{g:02x}{b:02x}"
        

    integer_ask = simpledialog.askinteger("Integer ask", "Please enter the number of string you want to generate")
    if integer_ask is not None:
        amount = integer_ask
        string_ask = simpledialog.askstring("String ask", "Please enter the desired text")
        if string_ask is not None:
            displayer = tk.Tk()
            frame = tk.Frame(displayer)
            frame.pack()
            for _ in range(amount):
                text_color = random_color()
                bg_color = random_color()

                label = tk.Label(frame, text = string_ask, font = ("Arial, 12"), fg = text_color, bg = bg_color)
                label.pack()

    

# Math root system

def math_window():
    root = tk.Toplevel()
    frame = tk.Frame(root)
    frame.pack()
    celsius_to_fahrenheit_menu_button = tk.Button(frame, text = "Celsius to Fahrenheit", command = math_window_celsius_to_fahrenheit, padx = 5, pady = 5)
    celsius_to_fahrenheit_menu_button.pack()
    cube_volume_menu_button = tk.Button(frame, text = "Cube volume measurer",command = math_window_cube_volume, padx = 5, pady = 5)
    cube_volume_menu_button.pack()

def math_window_celsius_to_fahrenheit():

    def celsius_to_fahrenheit():
        celsius = float(entry.get())
        fahrenheit = (celsius * 9 / 5) + 32
        result.config(text = f"{celsius}C is {fahrenheit}")

    def fahrenheit_to_celsius():
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5 / 9
        result.config(text = f"{fahrenheit}F is {celsius:.2f}C")

    root = tk.Tk()
    root.title("Celsius to Fahrenheit converter")
    root.geometry("350x200")
    entry = tk.Entry(root)
    entry.pack(pady = 10)
    frame = tk.Frame(root)
    frame.pack()

    #Button
    celsius_converter = tk.Button(frame, text = "Convert Celsius to Fahrenheit", command = celsius_to_fahrenheit)
    celsius_converter.grid(row = 0, column = 0, padx = 5)
    fahrenheit_converter = tk.Button(frame, text = "Convert Fahrenheit to Celsius", command = fahrenheit_to_celsius)
    fahrenheit_converter.grid(row = 0, column = 1, padx = 5)

    #Result
    result = tk.Label(root, text = "", font = ("Arial, 12"))
    result.pack(pady = 10)

def math_window_cube_volume():
    def cube_volume():
        side = int(entry.get())
        volume = side ** 3
        result.config(text = f"Volume {volume} is {side}^3")

    root = tk.Tk()
    root.title("Cube volume measurer")
    root.geometry("350x200")
    entry = tk.Entry(root)
    entry.pack(pady = 10)
    frame = tk.Frame(root)
    frame.pack()

    #Button
    cube_volume_converter = tk.Button(frame, text = "Convert cube side to volume", command = cube_volume)
    cube_volume_converter.grid(row = 0, column = 0, padx = 5)

    #Result
    result = tk.Label(root, text = "", font = ("Arial, 12"))
    result.pack(pady = 10)


# Utilty

#def windows_resizer():
   # new_width = event.width
   # new_height = event.height

   # entry.config(width = new_width)
   # listbox.config(width = new_width, height = new_height)



top = tk.Tk()
frame = tk.Frame(top)
frame.pack()
top.title("Experimental")
password_dialog = simpledialog.askstring("Password", "Please enter password")


if password_dialog is None:
    print("No password has been entered, the application has been stopped")
    sys.exit()

elif "farhan" not in password_dialog:
    print("Wrong password, the application has been stopped")
    sys.exit()
    


button_1 = tk.Button(frame, text = "Matplotlib", command = matplotlib_windows)
button_1.grid(row = 0, column = 0, padx = 5)
button_2 = tk.Button(frame, text = "RGB", command = rgb_window)
button_2.grid(row = 0, column = 1, padx = 5)
button_3 = tk.Button(frame, text = "Math", command = math_window)
button_3.grid(row = 0, column = 2, padx = 5)
top.mainloop()
