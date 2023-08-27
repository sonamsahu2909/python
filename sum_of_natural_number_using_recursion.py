def recursum(number):
    if number == 0:
        return number
    return number + recursum(number-1)
   
number = int(input())
sum = 0
print(recursum(number))