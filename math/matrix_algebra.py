# Matrix Algebra
import numpy as np

# list each matrix
A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6,0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.array([[1], [8], [0], [5]])
a = 6

# Matrix Dimensions 
print
print '1. Matrix Dimenstions'
print
print 1.1, "A's dimensions are", A.shape
print 1.2, "B's dimensions are", B.shape
print 1.3, "C's dimensions are", C.shape
print 1.4, "D's dimensions are", D.shape
print 1.5, "u's dimensions are", u.shape
print 1.6, "w's dimensions are", w.shape

# Vector Operations
print
print '2. Vector Operations'
print
print 2.1, "u + v = ", np.add(u,v)
print 2.2, "u - v = ", np.subtract(u,v)
print 2.3, "  au  = ", np.multiply(a,u)
print 2.4, "u • v = ", np.tensordot(u,v)
print 2.5, "||u|| = ", np.linalg.norm(u)

# Matrix Operations
print
print '3. Matrix Operations'
print
print 3.1, "A + C   = not defined"
print 3.2, "A - C^T =", np.subtract(A, np.transpose(C))
print 3.3, "C^T+3D  =", np.add(np.transpose(C), np.multiply(3,D))
print 3.4, "  BA    =", np.dot(B,A)
print 3.5, " BA^T   = not defined"

#Optional
print
print 'Optional'
print
print 3.6, " BC  = not defined"
print 3.7, " CB  =", np.dot(C,B)
print 3.8, " B^4 =", np.power(B,4)
print 3.9, "AA^T =", np.dot(A,np.transpose(A))
print 3.10,"D^TD =", np.dot(np.transpose(D),D)
