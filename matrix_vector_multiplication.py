import numpy as np

# Identity Matrix
I = np.identity(2,int)
x = np.array([4,5])

b = np.dot(I,x)

print("Identity Matrix")
print(I, x, b)

# MVM
A = np.array([[1,0],[1,0]])
x = np.array([4,5])

b = np.dot(A,x)

print("Matrix")
print(A, x, b)

print("First Column/Row of A")
# get first column of matrix
print(A[:,0])
# get first row of matrix
print(A[0,:])
