#concatenate  ===========> joining two array

import numpy as np
a=np.array([1,2,3,4])
b=np.array([3,2,5,7])
c=np.concatenate((a,b))
print(c)


#
import numpy as np
a=np.arange(16).reshape(4,4)
b=np.array([[1,2,3,4],[4,5,6,8],[5,8,1,5],[78,89,5,6]])
c=np.concatenate((a,b))



