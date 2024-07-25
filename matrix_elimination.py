import numpy as np
from numpy.linalg import multi_dot

# TODO
# matrix_rank check if matrix is singular
# hahaha check if the matrix is full rank
# where the rank of the matrix (number of linearly independent columns/rows
# equals the min(column/row dimensions)
# if singular, do not run program
# if not singular, allow swaps between rows

import random

class Me:

	# Matrix elimination class
	
	# size of square matrix
	n = 0

	A = np.zeros((n,n)) # tuple is used to intialize (0,0) size matrix
	b = np.zeros(n)

	# Let [A]_{n,n} and [x]_{n,1}
	# where [A]_{n,n} * [x]_{n,1} = [b]_{n,1}
	

	def __init__(self, A : np.array, b : np.array):

		# check if matrix is square
		if A.shape[0] != A.shape[1]:
			return False
		else:
			self.n = A.shape[0]
		
		# check if size matches dimensions of b
		if self.n != b.shape[0]:
			return False

		# constructor intializes Me by copying input matrix A and vector b
		self.A = A
		self.b = b

		# produces the Upper triangular matrix from A
		# and the Elimination matrix to get there
		(self.U, self.E) = Me.elimination(self.A)
		
		# produces y by multiplying Elimination matrix by vector b.
		self.y = np.dot(self.E,self.b)
		
		# finds x vector using backwards substitution 
		self.x = Me.backward_sub(self.U, self.y)


	# shear matrix S_ij(c)
	# todo? turn into class so default size is 4
	def sm(size : int, i, j, c) -> np.array:
		S = np.identity(size)
		S[i,j]=c
		return S
	
	# returns Upper triangular matrix and final elimination matrix
	def elimination(A : np.array) -> tuple[np.array, []]:
		# checks if A is square
		if A.shape[0] != A.shape[1]:
			return False
	
		A_copy = A
		
		n = A.shape[0]
		
		# array of elementary matrices to provide a history of matrices
		E = []
		for j in range(0,n-1):
			# pivot
			p = A[j,j]
			
			# The shear matrices of one column
			S = np.identity(n) # [S]_{n x n} identity matrix
	
			# create j+1 -> n shear matrices and combine
			for i in range(j+1,n):
				# print(i,j)
				c = -1 * A[i,j] / p
				s = Me.sm(n,i,j,c)
				# append shear matrices to a single shear matrix
				S = np.dot(S,s) 
	
			# applies shear matrix to A => find new pivot and shear matrices
			A = np.dot(S,A)
	
			# Appends all (column) shear matrices to a single E matrix. where E * A = U
			E.append(S)
	
		#print(E)
		
		# converts each entry of E into a single matrix : 
		# this allows for debugging (history of each E matrix)
		temp = np.identity(n)
		for i in E:
			temp = np.dot(i,temp)
		E = temp
	
		U = np.dot(E,A_copy)
	
		return(U, E)
		
	# return [X]_{n,1} vector
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
	
	# truncate any matrix for specified range
	# usage:
	# 	s.U = Me.truncate(s.U)
	def truncate(A : np.array):
		for i in range(0,A.shape[0]):
			for j in range(0,A.shape[1]):
				if abs(A[i,j]) < 0.000000001:
					A[i,j] = 0
		return A

	# print original equation
	def p_a(self):
		print("A * x = b")
		print(self.A)
		print(self.x)
		print(self.b)
	
	# print elimination matrix
	def p_e(self):
		print("E")
		print(self.E)
	
	# print upper triangular equation
	def p_u(self):
		print("U * x = y")
		print(self.U)
		print(self.x)
		print(self.y)

	# print original equation and upper triangular equation
	def p(self):
		self.p_a()
		self.p_u()

	# __repr_(self,): # representation
	# rule of thumb: __repr__ is for developers, __str__ is for customers.

	def __str__(self, ): 
		s = str(self.A) + "\n" + str(self.x) + "\n" + str(self.b)
		return s


# Test Inputs
A1 = np.array([[1,0,0,0],[2,1,0,0],[3,5,1,1],[1,3,5,1]])
b1 = np.array([5,10,3,1])

# system
s1 = Me(A1,b1)

s1.p()
s1.p_e()

A2 = Me.rand_array(4,10)

s2 = Me(A2,b1)
s2.U = Me.truncate(s2.U)
s2.p()
