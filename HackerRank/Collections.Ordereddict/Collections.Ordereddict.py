from collections import OrderedDict

dictionary = OrderedDict()
n = int(input())

for _ in range(n):
    item, price = input().rsplit(" ", 1) # we use rsplit because we want to input our product that have 2 words, example : BANANA FRIES, the (" ") mean the separator was space, and (,1) act as the maximal seperator
    if item in dictionary:              # we use this to check if the item which we entered earlier already in the dictionary or not, if yes, than the rest of the code will be executed, and vice versa if it's not
        dictionary[item] = int(dictionary[item]) + int(price) # the dictionary[item] mean, we are accessing the key of what we input recently respectively, and at the same time accessing the value of the key
    else:
        dictionary[item] = price # if the item(key) is new or not already there, then the value item, and the value will be added

for key, value in dictionary.items(): # built in method to access the key and the value at the same time, if we don't use this, than the for logic will be failed to be executed because it's expecting to many value / arguments and can't unpack it
    print(key, value)                   # the built in .items is very important if we want to loop all of the iterable in the dictionary
