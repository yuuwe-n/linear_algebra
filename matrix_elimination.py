import numpy as np
from numpy.linalg import multi_dot

# shear matrix S_ij(c)
# turn into class so default size is 4
def sm(size : int, i, j, c) -> np.array:
	E = np.identity(size)
	E[i,j]=c
	return E

A = np.array([[1,0,0,0],[2,1,0,0],[3,5,1,1],[1,3,5,1]])
x = [5,10,3,1]

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

y = np.dot(E,x)

print(U)
print(y)

x3 = y[3]/U[3,3]
x2 = (y[2]-U[2,3]*x3)/U[2,2]
x1 = (y[1]-U[1,2]*x2-U[1,3]*x3)/U[1,1]
x0 = (y[0]-U[0,1]*x1-U[0,2]*x2-U[0,3]*x3)/U[0,0]

x = np.array([x0,x1,x2,x3])

print(x)

def backward_sub(U : np.array, y : np.array):
	n = U.shape[0]

	X = []	
	for i in range(0,n)[::-1]:
	#	print("i",i)
		x = y[i]
		for k in range(i+1,n):
	#		print("k",k)
			x = x - U[i,k]*X[k-n]
		x = x / U[i,i]
		X.append(x)

	# reverses list at the end
	X = X[::-1]

backward_sub(U,y)

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

