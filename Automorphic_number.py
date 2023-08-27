# 27. Write a code to find Automorphic number
# The square of 25 gives 625, since the last digits are 25 it is an automorphic number.

num = int(input("Enter a number you want to check:"))

num_of_digits = len(str(num))
square = num**2
last_digit = square%pow(10,num_of_digits)

if(last_digit == num ):
    print("yes, {} is a automorphic number".format(num))
else:
    print("No , {} is not a automorphic number".format(num))