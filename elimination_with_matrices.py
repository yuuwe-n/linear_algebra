import numpy as np

A = np.array([[1,-1,-1,1],[2,0,2,0],[0,-1,-2,0],[3,-3,-2,4]])
b = np.array([0,8,-8,7])

E1 = np.identity(4,int)
E1[1,0] = -2

E2 = np.identity(4,int)
E2[3,0] = -3

E3 = np.identity(4)
E3[2,1] = 0.5

E4 = np.identity(4,int)
E4[2,2]=0
E4[2,3]=1
E4[3,3]=0
E4[3,2]=1

print("E4")
print(E4)
print("E3")
print(E3)
print("E2")
print(E2)
print("E1")
print(E1)
print()
print("A")
print(A)

E = np.dot(E4,np.dot(E3,np.dot(E2,E1)))
#E[3,0] = 0
print("E")
print(E)

B = np.dot(E,A)
print("B")
print(B)

#c = np.dot(E4,np.dot(E3,np.dot(np.dot(E2,E1),b)))
c = np.dot(E,b)
print("b")
print(b)
print("c")
print(c)

x3 = c[3]/B[3,3]
x2 = (c[2]-B[2,3]*x3)/B[2,2]
x1 = (c[1] - B[1,2]*x2 - B[1,3]*x3)/B[1,1]
x0 = (c[0] - B[0,1]*x1 - B[0,2]*x2 - B[0,3]*x3)/B[0,0]

print("x3 = ",x3)
print("x2 = ",x2)
print("x1 = ",x1)
print("x0 = ",x0)
