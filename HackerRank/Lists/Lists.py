if __name__ == "__main__":
    storage = [] # First we make an empty list
    n = int(input())

    for _ in range(n):
        command = input().split() # This the for the command we're going to run
        if "insert" in command[0]: # in this case, the questions want the input to be like this ; example : insert 0 5
            storage.insert(int(command[1]), int(command[2])) # so we make the command to be a list with .split(), and use every respective
        elif "print" in command[0]:                         # index to execute all of the other code, You can understand the code aside if you look closely at it
            print(storage)
        elif "remove" in command[0]:
            storage.remove(int(command[1]))
        elif "append" in command[0]:
            storage.append(int(command[1]))
        elif "sort" in command[0]:
            storage.sort()
        elif "pop" in command[0]:
            storage.pop()
        elif "reverse" in command[0]:
            storage.reverse()
