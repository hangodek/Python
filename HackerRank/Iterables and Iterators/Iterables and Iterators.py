if __name__ == "__main__":

    import itertools # We use the itertool module to loop the iterable without using many for and if else loop

    n = int(input())
    storage = list(input().split())
    indices_range = int(input()) # the range of iterable item that we want to iterate from the start of index
    counter = 0 # the 2 required value to get the division probability
    rounder = 0 #

    for i in itertools.combinations(storage, indices_range): # this is the module sub function, the combinations act as iterable combinationer, example if  we use the indices range 2, and iterable is 'A', 'B', 'C', then the 
        counter += 1                                            # the combiantioner will test for the probabilty of combination from a and b
        if 'a' in i:            # we want the iterable a, you can adjust this to your liking
            rounder += 1

print(rounder / counter)