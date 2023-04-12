import numpy as np
a=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(a)
print(a.ndim)
print(a.shape)

print('*'*1000)

#(3*4)
# to change thwe order of the matrix ======> (4*3) so we use
# reshape
print(a.reshape(4,3))

b=a.reshape([6,2])
print(b)

#not all elements cannot be reshaped only the total elements coluld be take part in it.
