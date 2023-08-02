
#Variation 1
'''from collections import namedtuple

n, Student = int(input()), namedtuple('Student', input().split())
print("{:.2f}".format(sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n ))
'''

#Variation 2
from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().split())

Student_Variable = [int(Student(*input().split()).MARKS) for _ in range (n)] #.MARKS yang ada setelah *input() untuk mengunpack
Student_Total = sum(Student_Variable)                                          # list, karena jika tidak pakai * , list tidak dapat dibaca
Student_Average = Student_Total / n

print("{:.2f}".format(Student_Average))











