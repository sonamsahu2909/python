# 24. Write code to check a String is palindrome or not?

def ispalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = ispalindrome(s)

if ans:
    print("yes")
else:
    print("No")