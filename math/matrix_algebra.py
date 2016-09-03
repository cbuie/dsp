# Matrix Algebra

import numpy as np

a = [1,2,3,2,7,4]
b = [1,-1,0,1]
c = [5,-1,9,1,6,0]
d = [3,-2,-1,1,2,3]
u = [6,2,-3,5]
v = [3, 5, -1, 4]
w = [1,8,0,5]

A = np.reshape(a, (2,3))
B = np.reshape(b,(2,2))
C = np.reshape(c,(3,2))
D = np.reshape(d,(2,3))

for i in [A,B,C,D]: print i