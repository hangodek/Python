import math # We can use this module with math.xxx, but the code gonna be a little long, you can search about the module in the internet
            # or you can look for the module command with dir module

if __name__ == '__main__': # to check either this code were imported or not, if not, then the code below will be executed, if yes then the code below will be skipped
    a = int(input())    # Requesting input from the users
    b = int(input())    
    
    summary = a + b
    difference = a - b
    productoftwo = a * b
    
    if a and b:
        print(summary) # we can print multiple variable at the same time like (x, x, x), but in this case, we want to make the code
        print(difference) # a little more readable
        print(productoftwo)
    
    