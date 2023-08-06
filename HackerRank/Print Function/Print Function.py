import re

if __name__ == '__main__':
    
#Variation 1    
    
    n = int(input())
    value = []
    
    for i in range(1, n + 1):   #We use for, to loop the value we're inputting to the n variable, and then changing the int value
        value.append(str(i))       # to string and append or add it to the value.
    
    print ("".join(value))      # We use the "".join method to print the item in the value without any ' / "" and ,
    
    
#Variation 2 
#n = int(input())
#    for i in range (1, n + 1):
#        print(i, sep= '', end='') # This is the more advanced variation, we directly print the i variable by using the separator
                                    # and end command to remove any ' / "" and ,
    