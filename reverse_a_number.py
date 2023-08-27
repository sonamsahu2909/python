# Write a code to reverse a number

num = int(input("enter the number:"))
reverse = 0
while num > 0:
    remainder = num % 10 
    reverse = (reverse * 10) + remainder 
    num = num  // 10
    
print("The reverse number is:{}".format(reverse))
             
                # or
             
# num = int(input("Enter the Number:"))
# temp = num
# reverse = 0
# while num > 0:
#     remainder = num % 10
#     reverse = (reverse * 10) + remainder
#     num = num // 10

# print("The Given number is {} and Reverse is {}".format(temp, reverse))   