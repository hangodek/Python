import math # Optional, if you want to use math.addition, math.substract, div, or another only

#Variation 1

if __name__ == '__main__': # Act as a code detector, either it's an imported code or not
    a = int(input())
    b = int(input())
    
    int_div = int(a / b)
    float_div = float(a / b)
    
    if a and b: # if a & b have a value or has been runned, the code below will be runned by the IDE
        print(int_div)
        print(float_div)
        
#Variation 2 (Shorter)                           # You can see more code variation from here to bottom
#if __name__ == '__main__':                      # with each variation shorter than another
  #  a = int(input())                           
  #  b = int(input())
    
  #  print(int(a / b), float(a / b))
  
""" Variation 3 (Even Shorter)
a = int(input())
b = int(input())
print(a//b)
print(a/b)
"""