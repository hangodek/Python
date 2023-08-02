""" 
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
    score = list(set(arr))
    score.sort(reverse = True)
    score.append(n)
    
    
    if len(score) >= 2:
        print(score[1])
    else:
        print(None)