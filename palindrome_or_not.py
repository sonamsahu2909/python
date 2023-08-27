#  Write code Check if the given string is Palindrome or not

string1 = input('Enter the String')
string2 = string1[::-1]
if string1 == string2:
    print('string is palindrone')
else:
    print('string is not palindron')