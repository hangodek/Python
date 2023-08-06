# Variation 2 (Advance)

if __name__ == '__main__':

    score_list = []
    combined_list = []

    for _ in range(int(input())): # To loop the code below as much as we put in to the input
        name = input()
        score = float(input())

        score_list.append(score)
        combined_list.append([name, score]) # Name index 0, and score index 1

    score_list = sorted(score_list)
    low_score = min(score_list) # The lowest possible value from the score_list
    score_list_sorted = []
    combined_list_sorted = []
    
    for i in (score_list):
        if low_score != i:
            score_list_sorted.append(i)
    
    for i in range(len(combined_list)):                         # Loop the code in range of as many values are in the list
        if score_list_sorted[0] == combined_list[i][1]:         # The [i][1] mean the combined_list that in the i variable or i
            combined_list_sorted.append(combined_list[i])       # 0 stand for the student name, and 1 stand for the score

    result = []
    for i in range(len(combined_list_sorted)):
        result.append(combined_list_sorted[i][0])
    result = sorted(result)
    for i in result:
        print(i)

"""
# Variation 2 (A little easier)

student_list = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    student_list.append([name, score]) # In this variation, we directly input the name and the score to the list

student_list.sort(key=lambda x: x[1])

second_lowest_score = sorted(set([x[1] for x in student_list]))[1]

for name, score in sorted(student_list):

    if score == second_lowest_score:
        print(name)

I still didn't understand about the lambda """        