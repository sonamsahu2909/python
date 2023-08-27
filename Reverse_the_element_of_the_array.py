# 30. Write a code to Print the smallest element of the array

arr = [10,31,42,9,32,43]
mini = arr[0]

for i in range(len(arr)):
    if arr[i] < mini:
        mini = arr[i]
print(mini)