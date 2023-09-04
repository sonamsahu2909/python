# # Write code of Greatest Common Divisor 

# num1 = int(input("Enter First Number:"))//20
# num2 = int(input("Enter Second Number:"))//30

# def gcdfunction(num1,num2):
#     if num1 > num2:
#         small = num2
#     else:
#         small = num1
    
#     for i  in range(1, small+1):
#         if (num1 % i == 0) and (num2 % i == 0):
#             gcd = i
#     return gcd
#     # print("GCD of two number: {}".format(gcd))

# gcdfunction(num1,num2)

# def gcdfunction(a, b):
#     while b:
#         a, b = b, a % b
#     return a

def gcdfunction(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd_result = gcdfunction(num1, num2)
print("Greatest common divisor:", gcd_result)
