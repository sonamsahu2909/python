# 31. Write a code to Reverse the element of the array

def reverselist(a,start,end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start +=1
        end-=1

a= [10,20,34,45,64]
print(a)
reverselist(a,0,4)
print("Reverse list is",a)