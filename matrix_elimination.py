import numpy as np
from numpy.linalg import multi_dot

import random

class Me:
	
	# size of square matrix
	n = 0

	A = np.zeros((n,n))
	b = np.zeros(n)
	
	def __init__(self, A : np.array, b : np.array):
		if A.shape[0] != A.shape[1]:
			return False
		else:
			self.n = A.shape[0]
		
		if self.n != b.shape[0]:
			return False
		
		self.A = A
		self.b = b

		(self.U, self.E) = Me.elimination(self.A)
		
		self.y = np.dot(self.E,self.b)
		
		self.x = Me.backward_sub(self.U, self.y)


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
				s = Me.sm(n,i,j,c)
				# append shear matrices to a single shear matrix
				S = np.dot(S,s) 
	
			# applies shear matrix to A => find new pivot and shear matrices
			A = np.dot(S,A)
	
			# Appends all (column) shear matrices to a single E matrix. where E * A = U
			E.append(S)
	
		#print(E)
		
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
	#		print("i",i)
			x = y[i]
			for k in range(i+1,n):
	#			print("k",k)
	#			print("k-n",k)
	#			print("-----")
				# access X backwards
				x = x - U[i,k]*X[k]
			x = x / U[i,i]
			X[i] = x
	
		return X
	
	# produces random matrix with max values of M
	def rand_array(n : int, M : int):
		A = np.zeros([n,n])
		
		for i in range(0,n):
			for j in range(0,n):
				a = random.randint(0, M)
				A[i,j] = a
		return A
	
	# truncate U => truncate any matrix for specified range
	def truncate():
		U = self.U
		for i in range(0,U.shape[0]):
			for j in range(0,U.shape[1]):
				if abs(U[i,j]) < 0.000000001:
					U[i,j] = 0

	# print original equation
	def p_a(self):
		print("A * x = b")
		print(self.A)
		print(self.x)
		print(self.b)
	
	def p_e(self):
		print("E")
		print(self.E)
	
	# print upper triangular equation
	def p_u(self):
		print("U * x = y")
		print(self.U)
		print(self.x)
		print(self.y)

	def p(self):
		self.p_a()
		self.p_u()


# Test Inputs
A = np.array([[1,0,0,0],[2,1,0,0],[3,5,1,1],[1,3,5,1]])
b = np.array([5,10,3,1])

system = Me(A,b)
system.p()

print(Me.elimination(A))
