# 20. Write the code to for Armstrong number

number = int(input("Enter a number: "))
num = number
digit, sum = 0, 0
length = len(str(num))
for i in range(length):
    digit = int(num%10)
    num = num/10
    sum += pow(digit,length)
if sum == number:
    print("Armstrong")
else:
    print("Not Armstrong")