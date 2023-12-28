import numpy as np
from numpy.linalg import multi_dot

import random

# shear matrix S_ij(c)
# turn into class so default size is 4
def sm(size : int, i, j, c) -> np.array:
	E = np.identity(size)
	E[i,j]=c
	return E


def elimination(A : np.array) -> tuple[np.array, []]:
	if A.shape[0] != A.shape[1]:
		return False

	A_copy = A
	
	n = A.shape[0]
	
	# array of elementary matrices
	E = []
	for j in range(0,n-1):
		p = A[j,j]
		
		# The shear matrices in one column
		S = np.identity(n)

		# create j+1 -> n shear matrices and combine
		for i in range(j+1,n):
#			print(i,j)
			c = -1 * A[i,j] / p
			s = sm(n,i,j,c)
			# append shear matrices to a single shear matrix
			S = np.dot(S,s) 

		# applies shear matrix to A => find new pivot and shear matrices
		A = np.dot(S,A)

		# Appends all (column) shear matrices to a single E matrix. where E * A = U
		E.append(S)
	
	# converts each entry of E into a single matrix
	temp = np.identity(n)
	for i in E:
		temp = np.dot(i,temp)
	E = temp

	U = np.dot(E,A_copy)

	return(U, E)
	

def backward_sub(U : np.array, y : np.array):
	n = U.shape[0]

	X = np.zeros(n)
	for i in range(0,n)[::-1]:
		print("i",i)
		x = y[i]
		for k in range(i+1,n):
			print("k",k)
			print("k-n",k)
			print("-----")
			# access X backwards
			x = x - U[i,k]*X[k]
		x = x / U[i,i]
		X[i] = x

	# reverses list at the end
#	X = X[::-1]
	return X

# produces random matrix with max values of M
def rand_array(n : int, M : int):
	A = np.zeros([n,n])
	
	for i in range(0,n):
		for j in range(0,n):
			a = random.randint(0, M)
			A[i,j] = a
	return A

# Test Inputs
#A = np.array([[1,0,0,0],[2,1,0,0],[3,5,1,1],[1,3,5,1]])
#b = [5,10,3,1]

#A = np.array([[1,0,0,1],[2,1,3,0],[3,8,1,1],[2,3,5,1]])
#b = [1315,10325,3123,1968]

#A = rand_array(5, 10)
#b = [53,103,33,29,26]

A = np.array([[2,1,0,0],[1,2,1,0],[0,1,2,1],[0,0,1,2]])
b = np.array([0,0,0,5])

U, E = elimination(A)

print(E)

y = np.dot(E,b)

x = backward_sub(U,y)

# truncate
for i in range(0,U.shape[0]):
	for j in range(0,U.shape[1]):
		if U[i,j] < 0.000000001:
			U[i,j] = 0

# print original equation
def p_a():
	print("A * x = b")
	print(A)
	print(x)
	print(b)

# print upper triangular equation
def p_u():
	print("U * x = y")
	print(U)
	print(x)
	print(y)

p_a()
print()
p_u()

