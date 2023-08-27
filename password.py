def isValid(str):
    length = len(str)
    l,u,n,d = 0,0,0,0
    if (length<8 or length>15):
        return False
    for i in str:
        if i==" ":
            return False
        if i.isupper():
            u=1
        elif i.islower():
            l=1
        elif not(i.isalnum()):
            d=1
        elif i.isnumeric():
            n=1
    if u==1 and l==1 and n==1 and d==1:
        return True
    return False
n = input() # CODiNGNinja+1 ,abcXyz 123,itsnotValid1
print(isValid(n))