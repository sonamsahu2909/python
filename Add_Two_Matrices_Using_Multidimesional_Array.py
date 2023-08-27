# 22. Write a program to add Two Matrices using Multi-dimensional Array.

matrix_a = [[1,2,3],
            [4 ,5,6],
            [7 ,8,9]]
 
matrix_b = [[1,2,3],
            [4 ,5,6],
            [7 ,8,9]]

#function for displaying matrix
def display(matrix):
   for row in matrix:
      print(row)
   print()

# Display two input matrices
print('The first matrix is defined as:') 
display(matrix_a)
print('The second matrix is defined as:')
display(matrix_b)

# Initializing Matrix with all 0s
result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

# Add two matrices 
for i in range(len(matrix_a)): 

   # iterate through rows 
   for j in range(len(matrix_a[0])):

      # iterate through columns
      result[i][j] = matrix_a[i][j] + matrix_b[i][j]

print('The addition of two matrices is:')
display(result)