import numpy as np
from numpy.linalg import multi_dot

# shear matrix S_ij(c)
# turn into class so default size is 4
def sm(size : int, i, j, c) -> np.array:
	E = np.identity(size)
	E[i,j]=c
	return E

A = np.array([[1,0,0,0],[2,1,0,0],[3,5,1,1],[1,3,5,1]])

def elimination(A : np.array) -> tuple[np.array, []]:
	if A.shape[0] != A.shape[1]:
		return False
	
	n = A.shape[0]
	
	# array of elementary matrices
	E = []
	for j in range(0,n-1):
		p = A[j,j]
		
		# The shear matrices in one column
		S = np.identity(n)
		for i in range(j+1,n):
#			print(i,j)
			c = -1 * A[i,j] / p
			s = sm(n,i,j,c)
			# append shear matrices to a single shear matrix
			S = np.dot(S,s) 
		#	print(s)
#		print(S)
		# Appends all shear matrices to a single E matrix. where E * A = U
		E.append(S)

	# converts each entry of E into a single matrix
	temp = np.identity(n)
	for i in E:
		temp = np.dot(i,temp)
	E = temp

	U = np.dot(E,A)

	return(U, E)
	
U, E = elimination(A)
print(U)


def backward_sub(U : np.array,y : np.array):
	print(U.shape[0])
	print(U)	

#backward_sub(U,y)

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

#p_a()
#print()
#p_u()

