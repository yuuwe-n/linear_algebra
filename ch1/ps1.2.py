import numpy as np

A = np.array([[1,0,0,0],[1,1,0,0],[1,2,1,0],[1,3,3,1]])

E1 = np.identity(4,int)
E1[1,0] = -1
E1[2,0] = -1
E1[3,0] = -1

E2 = np.identity(4,int)
E2[2,1] = -1
E2[3,1] = -1

E3 = np.identity(4,int)
E3[3,2] = -1

B1 = np.dot(E1,A)
B2 = np.dot(E2,B1)
B3 = np.dot(E3,B2)
E = np.dot(E3,np.dot(E2,E1))

E4 = np.identity(4,int)
E4[2,1] = -1
E4[3,1] = -1

E5 = np.identity(4,int)
E5[3,2] = -2

M = np.dot(E5,np.dot(E4,E))

A1 = np.dot(E,A)
A2 = np.dot(E4,A1)
A3 = np.dot(E5,A2)


print(A)
print(E1)
print(E2)
print(E3)
print(B1)
print(B2)
print(B3)
print(E)
print(A1)
print(E4)
print(A2)
print(E5)
print(A3)
print(M)
