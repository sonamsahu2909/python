# 11. Write to code to check whether a given year is leap year or not.

year = int(input("Enter Year:"))
if (year%4 == 0) and (year%400==0 or year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")