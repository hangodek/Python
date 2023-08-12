import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # The age of cars
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] # The speed of every cars

#We're going to generate the relationship value of this numbers

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))
print(r) # -0.75 mean there is a relationship, but it's not perfect

