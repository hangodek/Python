if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line)) # map is python built in fuction that we use to transform the line inputted value to a float at the same time(because the line gonna be a list(note : input().split())
        student_marks[name] = scores        # and transform it back to be a new list
    query_name = input()                # after that we make the respectively key and value for the empty dictionary which we have done before
                            # query_name serves as variabel name storage function area that we're going to use for the for and if logic

    for key,value in student_marks.items():     # we loop the key and value from sthe student_marks list or set, and use the builtin items function to loop through all of the iterable
        if key == query_name:           # if the query_name is the same as the key value that we has been looped through, then the if code will be executed
            result = sum(student_marks[query_name]) # we use sum to calcualte all of the value that in the student_marks with respective key
                
    
    print("{:.2f}".format(result / 3))      # then we use the format built in method to print the result variable with decimal numbers

            
            
