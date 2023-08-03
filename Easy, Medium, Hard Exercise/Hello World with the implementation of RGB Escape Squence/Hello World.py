""" Questions 

Level: Easy

Create a simple program to print the message "Hello, World!" to the screen.

Level: Medium

Modify the previous program to print the message "Hello, [username]!" by asking the user to enter their name.

Level: Difficult

Create a program that prints the message "Hello, World!" n times, where n is a number entered by the user.

Create a program that prints the message "Hello, World!" with random text and background colors each time the program is executed.

"""


#Exercise 1
print("Hello, World!")

#Exercise 2
name = input()
print("Hello,", name)

#Exercise 3

import random

def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def randomtext(text):
    text_color = randomcolor()
    bg_color = randomcolor()

    text_format = f"\033[38;2;{text_color[0]};{text_color[1]};{text_color[2]}m" #\033 is Escape Squence
    bg_format = f"\033[48;2;{bg_color[0]};{bg_color[1]};{bg_color[2]}m"         # 38;2; / 48;2; is 24 bit things together with m
    format_text = f"\033[0m"

    print(f"{text_format}{bg_format}{text}{format_text}")

if __name__ == "__main__":
    n = int(input())
    inputtext = (input())
    

    for _ in range(n):
        randomtext(inputtext)


    