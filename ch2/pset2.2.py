import numpy as np
b = np.array([8,20,0])
E1 = np.identity(3,int)
E2 = np.identity(3,int)
E1[1,0] = -2
E2[2,1] = 2
print(E1)
print(E2)
y = np.dot(E2,np.dot(E1,b))
print(y)
A = np.array([[2,3,1],[4,7,5],[0,-2,2]])
U = np.dot(E2,np.dot(E1,A))
print(U)
x2 = y[2]/U[2,2]
print(x2)
x1=(y[1]-U[1,2]*x2)/U[1,1]
print(x1)
x0=(y[0]-U[0,1]*x1-U[0,2]*x2)/U[0,0]
print(x0)

