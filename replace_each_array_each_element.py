# 15. Write a code to replace each element in an array by its rank in the array

def changeArr(input1):
 
    newArray = input1.copy()
    newArray.sort()
     
    for i in range(len(input1)):
        for j in range(len(newArray)):
            if input1[i]==newArray[j]:
                input1[i] = j+1
                break
    
# Driver Code
arr = [100, 2, 70, 12 , 90]
changeArr(arr)
# Print the array elements
print(arr)