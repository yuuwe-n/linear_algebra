import numpy as np

from matrix_elimination import Me

A = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
b = np.array([1,1,1,1])

system = Me(A,b)

system.p()
