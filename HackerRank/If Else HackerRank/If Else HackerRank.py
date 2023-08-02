import math
import re
import sys
import os
import random

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 == 0:
        if n > 20:
            print ("Not Weird")
        
        elif n in range (2, 6):
            print ("Not Weird")
        
        elif n in range (6, 21):
            print ("Weird")
    
    else :
        print ("Weird")
       
        