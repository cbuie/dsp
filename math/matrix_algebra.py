# Matrix Algebra

import numpy as np

a = [1,2,3,2,7,4]
b = [1,-1,0,1]
c = [5,-1,9,1,6,0]
d = [3,-2,-1,1,2,3]
u = np.array([6,2,-3,5])
v = np.array([3, 5, -1, 4])
w = np.array([1,8,0,5])

A = np.reshape(a, (2,3))
B = np.reshape(b,(2,2))
C = np.reshape(c,(3,2))
D = np.reshape(d,(2,3))


#print dimensions of objects:
n = 0
for i in [A,B,C,D,u,w]:
    n += 1
    print '1.'+str(n)+': '+str(i.shape)


#2.1 u + v
print '2.1:',u + v


#2.2 u - v
print '2.2:',u - v


#2.3 alpha u
alpha = 6
print '2.3:',alpha*u


#2.4 u*v
print '2.4:',u*v


#2.5 ||u||
print '2.5:',np.linalg.norm(u)


#3.1
print '3.1:', A+C



#3.2
print '3.2:', A-np.transpose(C)


#3.3
print '3.3:', np.transpose(C) + 3*D


#3.4
print '3.4:', B*A


#3.5
print '3.5:', B*np.transpose(A)


#3.6
print '3.6:', np.dot(B*C)


#3.7
print '3.7:', np.dot(C,B)


#3.8
print '3.8:', B**4

#3.9
print '3.9:', np.dot(A,np.transpose(A))



#3.10
print '3.10:', np.dot(np.transpose(D),D)
