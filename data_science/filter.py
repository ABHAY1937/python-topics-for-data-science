import numpy as np
a=np.arange(10)
print(a)
# print(np.where(b>5),filter)
# print(np.where(b%2==0),filter)
#
b=a%2==0
c=a[b]
print(c)
