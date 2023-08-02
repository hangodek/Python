import math
import os
import sys
import re
import random

if __name__ == '__main__':
    
    def is_leap(year):
        leap = False
    
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 == 0:
                leap = True
            elif year % 100 == 0 and year % 400 != 0:
                leap = False
            elif year % 100 != 0:
                leap = True

        return leap
        
year = int(input())
print(is_leap(year))