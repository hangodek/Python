if __name__ == "__main__":

    from collections import Counter # Well, i try to make the code but i am confused about the logical things that we're gonna use to count the difference occurence between the showing up words
    dictionary = []                 # then i give up and looked at the discussion column.. and.. bamm... all of this people we're using this module... i am fucked up...
                                    # well, this module act as a counter of the difference occurence between the value or string in the list
    n = int(input())

    for _ in range(n):
        temporary = input()
        dictionary.append(temporary)

print(len(Counter(dictionary).keys()))
print(*Counter(dictionary).values())    # We use the print(*) as always, if you didn't know yet.. it's used to unpack the item or value in list, so when we print it, the output not gonna have this thing [,.] etc..
