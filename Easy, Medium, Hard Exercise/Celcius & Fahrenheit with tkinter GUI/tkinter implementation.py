""" Questions 

Easy:
Write a Python function that takes a temperature in Celsius as input and returns the corresponding temperature in Fahrenheit. The conversion formula is:

Fahrenheit = (Celsius * 9/5) + 32

Medium:
Create a Python program that prompts the user to enter a temperature in Celsius and then converts it to Fahrenheit. After displaying the result, ask the user if they want to perform another conversion. Keep the program running until the user decides to exit.

Hard:
Build a Python GUI application using Tkinter that allows the user to enter a temperature in Celsius. The application should have a "Convert" button that, when clicked, displays the converted temperature in Fahrenheit. Additionally, include a feature to toggle between Celsius and Fahrenheit, so the user can switch between conversions without closing the application.

Remember to prompt the user for input, handle potential errors, and format the output appropriately.

"""

"""Exercise 1
print("Celcius to Fahrenheit converter")
celcius = int(input("Enter celcius value : "))
fahrenheit = (celcius * 9 /5 ) + 32
print("The fahrenheit value is ", fahrenheit)

"""

"""Exercise 2

import sys

def newinput():
    yes = input("Do you want to calculate another value ? ").lower()
    if "yes" in yes:
        main()
    else:
        print("Program has been stopped ! ")
        sys.exit()
def main():
    print("Celcius to Fahrenheit converter")
    celcius = int(input("Enter celcius value : "))
    fahrenheit = (celcius * 9 / 5 ) + 32
    print("The fahrenheit value is ", fahrenheit)

    if fahrenheit:
        newinput()
            

if __name__ == '__main__':
    main()

"""

#Exercise 3

import tkinter as tk

def celsius_to_fahrenheit():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9 / 5) + 32
    result_label.config(text = f"{celsius}C is {fahrenheit}F")

def fahrenheit_to_celsius():
    fahrenheit = float(entry.get())
    celsius = (fahrenheit - 32) * 5 / 9
    result_label.config(text = f"{fahrenheit}F is {celsius}C")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

entry = tk.Entry(root)
entry.pack(pady = 10)

frame = tk.Frame(root)
frame.pack()

celsius_button = tk.Button(frame, text="Celsius to Fahrenheit", command = celsius_to_fahrenheit)
celsius_button.grid(row = 0, column = 0, padx = 5)

fahrenheit_button = tk.Button(frame, text="Fahrenheit to Celsius", command = fahrenheit_to_celsius)
fahrenheit_button.grid(row = 0, column = 1, padx = 5)

result_label = tk.Label(root, text = "", font=("Arial", 12))
result_label.pack(pady = 10)

menu = tk.Menu(root)
root.config(menu = menu)

temperature_menu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Temperature", menu = temperature_menu)

temperature_menu.add_command(label = "Celsius to Fahrenheit", command = celsius_to_fahrenheit)
temperature_menu.add_command(label = "Fahrenheit to Celsius", command = fahrenheit_to_celsius)

root.mainloop()





