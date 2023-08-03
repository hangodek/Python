if __name__ == '__main__':
    
    def is_leap(year): # This is non-built in function that we make to call our code without typing too much
        leap = False
    
        if year % 4 == 0:                                   # This code is have a similiarity with the previous code we make (Weird, not Weird)
            if year % 100 == 0 and year % 400 == 0:         # that is "Modulo"
                leap = True                                 
            elif year % 100 == 0 and year % 400 != 0:       # First, we check and detect if the year value in the is_leap definition
                leap = False                                # can be divided until zero or not, if it can, than nested if will be runned
            elif year % 100 != 0:                           
                leap = True                                 # From my self understanding upon the questions, we know that it's not gonna be a leap_year
                                                            # if the value can be evenly divided by 100.. but.. we have another condition
        return leap                                         # if the value can be evenly divided by 100, and at the same time can be divided by 400
                                                            # gotcha, it's gonna be a leap year, so we place True bool at the first index nested if
year = int(input())                                         # now, if the number one index if doesn't meet the requirement, the program gonna read the next     
print(is_leap(year))                                        # nested if(elif), if the year can evenly divided by 100 but can't evenly divided by 400
                                                            # than the elif will give leap(variable) False bool.
                                                            # now, we're at the last nested if(elif), if the year value can't evenly divided by 100
                                                            # than the (if) top code will not run and the leap(variable) will stay False