# 18. Write a code to check for the longest palindrome in an array.

def longest_palindrome(arr):
    pal = -1
   
    for i in arr:
        if str(i) == str(i)[::-1]:
            if i>pal:
                pal = i
        else:
            pass
    return pal
  
arr = [1,121,13341,1334331,13431,2313,4,2]
print(arr)
print("longest palindrome is : ",longest_palindrome(arr))