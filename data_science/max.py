import numpy as np
a=np.arange(10)
print(a)
print(np.max(a)) #returning the highest value
print(np.min(a))

print('*'*100)

#in 2D array
import numpy as np
b=np.arange(10,22,2).reshape(3,2)
print(b)
print(np.max(b))
print(np.min(b))
print(np.max(b,axis=1))
print(np.max(b,axis=0))
print(np.min(b,axis=0))
print(np.min(b,axis=1))
print(np.argmax(b))