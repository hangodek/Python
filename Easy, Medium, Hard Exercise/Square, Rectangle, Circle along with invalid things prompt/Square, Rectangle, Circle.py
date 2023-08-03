""" Questions 

Level: Easy

Create a simple program to calculate the area of a square. The program should prompt the user to enter the side length of the square and then display the calculated area.

Level: Medium

Enhance the previous program to allow the user to choose the shape (square, rectangle, or circle) for which they want to calculate the area. After the user enters the shape, the program should prompt for the necessary dimensions and display the calculated area accordingly.

Level: Hard

Build a comprehensive area calculator program that can handle various shapes, including square, rectangle, circle, triangle, and trapezoid. The program should allow the user to choose the shape and then prompt for the required dimensions. After the user enters the dimensions, the program should display the calculated area for the chosen shape. Additionally, the program should have error handling to handle invalid input and ensure the entered dimensions are valid for the selected shape.

"""

""" Exercise 1

a = int(input())
b = int(input())
result = a * b
print(result)

"""

"""Exercise 2

shape = input("What kind of shape do you want to calculate ? ")

if "Square" in shape:
    a = int(input("Side a value : "))
    b = int(input("Side b value : "))
    result = a * b
    print(result)

elif "Rectangle" in shape:
    a = int(input("Lenght of side a : "))
    b = int(input("Lenght of side b : "))
    result = a / b
    print(result)

elif "Circle" in shape:
    a = int(input("Radius : "))
    result = a ** 2 * 3.14
    print(result)

elif "Triangle" in shape:
    a = int(input("Triangle base : "))
    b = int(input("Triangle height : "))
    result = (a * b) / 2
    print(result)

elif "Trapezoid" in shape:
    a = int(input("Trapezoid side a : "))
    b = int(input("Trapezoid side b : "))
    c = int(input("Trapezoid height : "))
    result = (a + b) * c / 2
    print(result)

"""

#Exercise 3

def float_input_prompt(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter the correct value ! ")

def float_positive_input_prompt(prompt):
    while True:
        value = float_input_prompt(prompt)
        if value >= 0:
            return value
        print("Please enter positive number ! ")

def calculate_square_area(side):
    return side * side

def calculate_rectangle_area(lenght, width):
    return lenght / width

def calculate_circle_area(radius):
    return radius ** 2 * 3.14

def calculate_triangle_area(base, height):
    return (base * height) / 2

def calculate_trapezoid_area(side_a, side_b, height):
    return (side_a + side_b) * height / 2

def main():
    print("Area Calculator")
    print("Please choose available shape : Square, Rectangle, Circle, Triangle, Trapezoid")

    shape = input("Enter the shape you desire : ").lower()

    if shape == "square":
        side = float_positive_input_prompt("Enter the side value : ")
        area = calculate_square_area(side)
    elif shape == "rectangle":
        lenght = float_positive_input_prompt("Enter the lenght value : ")
        width = float_positive_input_prompt("Enter the width value : ")
        area = calculate_rectangle_area(lenght, width)
    elif shape == "circle":
        radius = float_positive_input_prompt("Enter the radius value : ")
        area = calculate_circle_area(radius)
    elif shape == "triangle":
        base = float_positive_input_prompt("Enter the base value : ")
        height = float_positive_input_prompt("Enter the height value : ")
        area = calculate_triangle_area(base, height)
    elif shape == "trapezoid":
        side_a = float_positive_input_prompt("Enter side a value : ")
        side_b = float_positive_input_prompt("Enter side b value : ")
        height = float_positive_input_prompt("Enter height value : ")
        area = calculate_trapezoid_area(side_a, side_b, height)
    else:
        print("Invalid shape, please choose an available shape !")
        return
    
    print("The area of", shape, "is :", area)
    
    

if __name__ == "__main__":
    main()







