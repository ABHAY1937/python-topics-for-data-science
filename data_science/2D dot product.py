import numpy as np
a=np.arange(1,17).reshape(4,4)
b=np.arange(16,32).reshape(4,4)
print(a)
print(b)
# 1st row to 2ndila 1 column  1*16 + 2* 20 +3*24+ 4*28
# [ 1  2  3  4]
# [ 5  6  7  8]
# [ 9 10 11 12]
# [13 14 15 16]]

# [16 17 18 19]
# [20 21 22 23]
# [24 25 26 27]
# [28 29 30 31]

c=np.dot(a,b)
print(c)