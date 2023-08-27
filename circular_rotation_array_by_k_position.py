# 16. Write a code to find circular rotation of an array by K positions.

def rotateArray(arr,n,d):
    arr[:] = arr[d:n] + arr[0:d]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)
print("Array after left rotation is: ",end=" ")
print(rotateArray(arr,len(arr),2 ))