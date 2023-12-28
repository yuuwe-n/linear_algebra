import numpy as np
from numpy.linalg import multi_dot

A = np.array([[2,1,0,0],[1,2,1,0],[0,1,2,1],[0,0,1,2]])

# Elementary Matrices
E1 = np.identity(4)
E1[1,0]=-.5

E2=np.identity(4)
E2[2,1]=-2/3

E3 = np.identity(4)
E3[3,2]=-3/4

# Upper Triangular
U=np.dot(E3,np.dot(E2,np.dot(E1,A)))

# Output vector
b=[0,0,0,5]
y = np.dot(E3,np.dot(E2,np.dot(E1,b)))

x3=y[3]/U[3,3]
x2=(y[2]-U[2,3]*x3)/U[2,2]
x1=(y[1]-U[1,2]*x2-U[1,3]*x3)/U[1,1]
x0=(y[0]-U[0,1]*x1-U[0,2]*x2-U[0,3]*x3)/U[0,0]
x = np.array([x0,x1,x2,x3])

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

A = np.array([[1,0,0],[2,1,0],[3,5,1]])

# shear matrix S_ij(c)
# turn into class so default size is 4
def sm(size : int, i, j, c) -> np.array:
	E = np.identity(size)
	E[i,j]=c
	return E

A = np.array([[1,0,0,0],[2,1,0,0],[3,5,1,1],[1,3,5,1]])

def elimination(A : np.array):
	if A.shape[0] != A.shape[1]:
		return False
	
	n = A.shape[0]
	
	E = []
	for j in range(0,n-1):
		p = A[j,j]
		
		# The shear matrices in one column
		S = np.identity(n)
		for i in range(j+1,n):
			print(i,j)
			c = -1 * A[i,j] / p
			s = sm(n,i,j,c)
			# append shear matrices to a single shear matrix
			S = np.dot(S,s) 
		#	print(s)
		print(S)
		# Appends all shear matrices to a single E matrix. where E * A = U
		E.append(S)
	print(E)
	for i in E:
		A = np.dot(i,A)

	print(A)
	
#	p_0 = A[0,0]
#	c_10 = -1 * A[1,0] / p_0
#	S_10 = sm(3,1,0,c_10)
#	
#	c_20 = -1 * A[2,0] / p_0
#	S_20 = sm(3,2,0,c_20)

#	return(multi_dot([S_20,S_10,A]))
#	return(np.dot(S_20,np.dot(S_10,A)))

elimination(A)
