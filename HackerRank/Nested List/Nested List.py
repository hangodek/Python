if __name__ == '__main__':

    score_list = []
    combined_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        score_list.append(score)
        combined_list.append([name, score])

    score_list = sorted(score_list)
    low_score = min(score_list)
    score_list_sorted = []
    combined_list_sorted = []
    
    for i in (score_list):
        if low_score != i:
            score_list_sorted.append(i)
    
    for i in range(len(combined_list)):
        if score_list_sorted[0] == combined_list[i][1]:
            combined_list_sorted.append(combined_list[i])

    result = []
    for i in range(len(combined_list_sorted)):
        result.append(combined_list_sorted[i][0])
    result = sorted(result)
    for i in result:
        print(i)

"""
student_list = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    student_list.append([name, score])

student_list.sort(key=lambda x: x[1])

second_lowest_score = sorted(set([x[1] for x in student_list]))[1]

for name, score in sorted(student_list):

    if score == second_lowest_score:
        print(name)

I still didn't understand about this """        