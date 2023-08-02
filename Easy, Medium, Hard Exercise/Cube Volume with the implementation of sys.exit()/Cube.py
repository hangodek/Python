""" Questions 

Level: Easy

Write a Python function called calculate_cube_volume that takes the length of the side of a cube as input and returns its volume.

Create a Python program that calculates and prints the volume of a cube with a side length of 5 units.

Level: Medium

Write a Python program that takes user input for the side length of a cube and then prints its volume. Handle any input errors gracefully.

Create a Python function called calculate_cube_surface_area that takes the length of the side of a cube as input and returns its surface area.

Level: Hard

Implement a Python class called Cube that has methods to get the volume and surface area. The class should be initialized with the length of the cube's side. Test the class by creating a cube object and calculating its volume and surface area.

Create a comprehensive Python program that allows the user to choose between calculating the volume or surface area of a cube. After the user makes a choice, prompt for the necessary dimensions and display the calculated value accordingly. Handle any input errors gracefully and provide clear instructions to the user.

"""

"""Exercise 1

def calculate_cube_volume():
    length = float(input("Enter the length of cube : "))
    volume = length ** 3
    print(volume)

calculate_cube_volume()

"""

"""Exercise 2
import math
import sys

def inputchecker(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number ! ")

def positiveinputchecker(prompt):
    while true:
        value = inputchecker(prompt)
        if value >= 0:
            return value
        print("Please enter non-float value ! ")

def calculate_cube_volume(length):
    return length ** 3

def calculate_cube_surface(length):
    return 6 * (length ** 2)

def main():
    print("Cube volume calculator")
    
    yesno = input("Please input y to execute the program ! ")
    
    if yesno == "y":

        length = inputchecker("Please enter the length of cube : ")
        volume = calculate_cube_volume(length)
        surface = calculate_cube_surface(length)

        print("The volume for cube is ", volume, "and the surface value is ", surface)

    else:
        print("The program has been stopped ! ")
        sys.exit()


if __name__ == '__main__':
    main()
    
"""

import sys

def inputchecker(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number ! ")

def positive_input(prompt):
    while True:
        value = inputchecker(prompt)
        if value >= 0:
            return value
        print("Please input non-float number ! ")

def calculate_cube_volume(length):
    return length ** 3

def calculate_cube_surface(length):
    return 6 * (length ** 2)

def main():
    print("Cube calculator")
    print("Choose the calculation : Volume, Surface")

    n = input().lower()

    if n == "volume":
        length = positive_input("Input the length of cube : ")
        volume = calculate_cube_volume(length)
        print("The volume of the cube is ", volume)

    elif n == "surface":
        length = positive_input("Input the length of cube : ")
        surface = calculate_cube_surface(length)
        print("the surface of the cube is ", surface)

    else:
        print("The program has been stopped ! ")
        sys.exit()


if __name__ == '__main__':
    main()

    

    

    
