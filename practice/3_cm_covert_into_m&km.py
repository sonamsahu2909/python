# 6.write a c program enter length in centimetre and convert it into meter and kilometre

length = float(input("enter a length of centimeter"))
print("Centimeter to meter", format(length/100))
print("Centimeter to kilometer", format(length/(10**5)))
