
#Variation 1
'''from collections import namedtuple # The required module for namedtuple

n, Student = int(input()), namedtuple('Student', input().split()) # We can input n and at the same time we can make student namedtuple while inputting the value for the namedtuple which contain Ids, Name, Mark, and Class for each respective student 
print("{:.2f}".format(sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n )) # After inputting the number, finally we can use placeholder with :.2f format which will display the print out number for the sum with two digits behind
'''                                                                                        # we use the *(asterisks) in the beside code to unpack the value that we has been inputted to the student namedtuple so we can sum it

#Variation 2
from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().split()) # The 'Student' mean class for the namedtuple and cannot be left blank

Student_Variable = [int(Student(*input().split()).MARKS) for _ in range (n)] # Don't forget the asterisks, because if we didn't include it in our code
Student_Total = sum(Student_Variable)                                           # the code can't unpack the items which in the list / tuple 

print("{:.2f}".format(Student_Average))











