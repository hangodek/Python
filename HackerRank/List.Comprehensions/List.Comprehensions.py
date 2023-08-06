if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # Variation 1 (Advance)
    #value = [[i, j, k] for i in range (0, x+1) for j in range (0, y + 1) for k in range (0, z + 1) if not (i + j + k) == n] 
    #print(value)

    value = []                          # We use empty list that act as a data container that we're gonna loop trough and for so we can generate the value one by one for each variable like the questions asked us
    for i in range(0, x+1):             # We use 0 before x+1 to make sure we start the number from zero
        for j in range(0, y+1):         # so it will be 0, 1, and so on
            for k in range(0, z+1):
                if (i + j + k) != n:            # The questions asked us to make sure the variable is not as the same as the n, so if the condition
                    value.append([i, j, k])     # requirement has been meeted, the if logical will start the append to the empty list
    
    print(value)