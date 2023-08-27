# 12. Find non-repeating characters in a string

String = input("Enter a string:")
for i in String:
    count = 0
    for j in String:
        if i == j:
            count+=1
        if count > 1:
            break
    #print for nonrepeating characters
    if count == 1:
        print(i,end = " ")