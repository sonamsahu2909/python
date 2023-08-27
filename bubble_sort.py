# Write a code for bubble sort

def bubblesort(arr):
    swapped = False
    for n in range(len(arr)-1, 0, -1): 
        for i in range(n):
            if arr[i] > arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]       
        if not swapped:
            return
    
    
arr =[43,544,634,2,32,46,74]
print("unsorted list is,")
print(arr)
bubblesort(arr)
print("sorted array is:")
print(arr)
