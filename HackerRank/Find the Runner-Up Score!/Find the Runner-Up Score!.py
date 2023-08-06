""" 
# Varitaion 1 (A little complex)

if __name__ == '__main__':
     score = []
    n = int(input())
    arr = map(int, input().split())
    score.extend(arr)

    sorted_score = sorted(score, reverse = True)

    runner_up_score = None
    for score in sorted_score:
        if score < max(sorted_score): 
            runner_up_score = sorted_score
            break

    if runner_up_score is not None:
        print(score)
    else:
        print(None)
    
 I dunoo why this code work :( """

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score = list(set(arr)) # We use this command to turn the arr to set (Removing all the duplicated number) and turning it back to a list
    score.sort(reverse = True)  # .sort is as same as sorted but a little simple    # so we get a clean free list without any duplicate number
    score.append(n)
    
    
    if len(score) >= 2: # if score has 2 or equal item inside it, then the print index 1 of the score list will be executed
        print(score[1])
    else:
        print(None)