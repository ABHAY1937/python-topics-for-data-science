#the 1st rows and 1st column should be equal nos for . product
import numpy as np
a=np.arange(1,10).reshape(3,3)
b=np.arange(1,7).reshape(3,2)
print(a)
print(b)
c=np.dot(a,b)
print(c)