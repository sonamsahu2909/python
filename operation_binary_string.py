def OperationBinaryString(str):
    if str is None:
        return -1
    
    # Initialize result with the first binary digit
    result = int(str[0])
    
    for i in range(1,len(str),2):
        operator =str[i]
        operand = int(str[i+1])
        
        if operator == 'A': # AND operation
            result = result and operand
        elif operator == 'B': # OR operation
            result = result or operand
        elif operator == 'C': # XOR operation
            result = result ^ operand
    return result

str = input() #  1C0C1C1A0B1 -1
print(OperationBinaryString(str))