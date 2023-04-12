#complex matrix or complex numbers matrix

#1.Real part
#2. imaginary part


#a+ib  ======>a real part  ,b===> imaginary part

#creating a complex number
import numpy as np
a=np.ones([3,4],dtype=complex) #dtype=complex convert this to a complex number format
print(a)

#creating a full matrix and to complex

import numpy as np
a=np.full([4,4],5,dtype=complex)
print(a)

print('*'*100)
#complex number with real part and imaginary part

import numpy as np
a=np.array([[2+3j,5+9j,9+8j],[1+6j,5+9j,8+7j]],dtype=complex)
print(a)