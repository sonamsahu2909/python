def Fibo(n):
    if n<0:
        print("Incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibo(n-1)+Fibo(n-2) 

#Main Program
print(Fibo(6))
