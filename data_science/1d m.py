#1D matrix
import numpy as np
a=np.arange(10)
print(a)
#sum
print(np.sum(a))

print('*'*100)
import numpy as np
b=np.arange(12).reshape(4,3)
print(b)
# [ 0  1  2]
# [ 3  4  5]
# [ 6  7  8]
# [ 9 10 11]
#axis=0 ====> sum of columns
#axis=1  ====> sum of rows
print(np.sum(b))
print(np.sum(b,axis=0))
print(np.sum(b,axis=1))

