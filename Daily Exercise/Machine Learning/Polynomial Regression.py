import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x, y, 3))

myline = np.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline)) # mymodel(myline) essentially takes each x value from the myline array and calculates the corresponding y value using the polynomial equation stored in the mymodel object.                          
plt.show()                          # This gives you a set of predicted y values that correspond to the x values in the myline array.

# When you use plt.plot(myline, mymodel(myline)), you're telling Matplotlib to plot the predicted y values (calculated using the polynomial regression model) against the x values from the myline array. 
# This creates the actual curve of the regression line on your plot.

#Searching the relationship between value before applying polynomial regression

print(r2_score(y, mymodel(x)))


#Predict the car that passing by at 17:00 PM
speed = mymodel(17)
print(speed)