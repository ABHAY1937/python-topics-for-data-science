import numpy as np
a=np.arange(10)
print(a)
#sort  ===arranging in ascending or decending order

print(np.sort(a))  #===>ascending order


#decending order
print(np.sort(a) [::-1])

#2D
import numpy as np
b=np.arange(16).reshape(4,4)
print(b)

print('*'*100)  #
print(np.sort(b,axis=1)) #row ways soarting / ascending order

print('*'*100)
print(np.sort(b,axis=0)) #column ways / decending order


