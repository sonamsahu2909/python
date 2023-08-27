# 17. Write a code to find non repeating elements in an array.

def nonRepeatingElement(arr):
    nonRepeatingElement = []
    for num in arr:
        if arr.count(num) == 1:
             nonRepeatingElement.append(num)
    return  nonRepeatingElement

arr = [1,2,4,5,6,6,7]
print(arr)
print("non repeating element is: ",nonRepeatingElement(arr))