#1 to 20  5*4 matrix

import numpy as np
a=np.arange(1,21).reshape([5,4])
print(a)

#2
import numpy as np
a=np.arange(1,21)
print(a)
print(a.reshape([5,4]))

print('*'*100)
#
import numpy as np
a=np.arange(1,100,2) #1D to change to higher Diamension
print(a.reshape(10,5))