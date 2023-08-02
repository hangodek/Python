import math
import re
import sys

#Variation 1

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    int_div = int(a / b)
    float_div = float(a / b)
    
    if a and b:
        print(int_div)
        print(float_div)
        
#Variation 2 (Shorter)
#if __name__ == '__main__':
  #  a = int(input())
  #  b = int(input())
    
  #  print(int(a / b), float(a / b))
  
""" Variation 3 (Even Shorter)
a = int(input())
b = int(input())
print(a//b)
print(a/b)
"""