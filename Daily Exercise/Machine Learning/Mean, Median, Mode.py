import numpy as np
from scipy import stats

speed = [86,87,88,86,87,85,86]
speed_2 = [32,111,138,28,59,77,97]
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = np.mean(speed)
y = np.median(speed)
z = stats.mode(speed)
std_low = np.std(speed)
std_high = np.std(speed_2)
variance = np.var(speed_2)
age_of_people_in_the_street = np.percentile(ages, 75)

print(x) # Mean is the average value
print(y) # Median is the number that in the middle, if the value is even, we can get the median by dividing the 2 middle value 
print(z) # Mode is number that appears frequntly
print(std_low) # Low standart deviation meaning that the value is not far away from the mean value
print(std_high) # High standart deviation meaning that the value is a little or more far away from the mean value
print(variance) # We can get variance value from square root of standart diviation
print(age_of_people_in_the_street) # 75% people are 43 or younger