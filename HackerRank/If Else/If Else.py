import math #Honestly all of this module doesn't do anything for this program that we're going to make
import re 
import sys
import os
import random

#Nb : Odd = Ganjil, Even = Genap

if __name__ == '__main__':
    n = int(input().strip())  #.strip() act a whitespace remover so we can make multiple input in one line
    
    if n % 2 == 0:  # % act as a modulo that calculate the remainder of the division between two number
        if n > 20:  # example 10 % 3, then the modulo is ; 1
            print ("Not Weird") # as what i know, we use modulo here because we want to detect either the n variable can be divided until zero
                                # or not, if the n variable can be, the if program will start the other nested if command
        elif n in range (2, 6): 
            print ("Not Weird")
        
        elif n in range (6, 21):
            print ("Weird")
    
    else :
        print ("Weird") # we pun the else "Weird" at the bottom because we know that if the number can be divided until equal to zero
                        # it's an odd number, so we put the else as the last nested if, so we can run the elif to check other
                        # requirement for the questions that hackerrank made for us.
       
        