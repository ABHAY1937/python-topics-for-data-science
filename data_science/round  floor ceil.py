#round floor ceil
import numpy as np
a=np.array([[1.02,2.02,4.06,4.26],[2.36,4.89,9.99,4.56],[1.02,2.02,4.06,4.26],[9.45,5.12,4.01,6.23]])
print(a)
#
# [1.02 2.02 4.06 4.26]
# [2.36 4.89 9.99 4.56]
# [1.02 2.02 4.06 4.26]
# [9.45 5.12 4.01 6.23]
print('*'*100)
#floor:to discard decimal part
print(np.floor(a))

print('*'*100)
#ceil =======>convert into highest integer
print(np.ceil(a))

print('*'*100)
#round
#0.5 above ===>highest
#0.5 below ======> lowest
print(np.round(a))

#0.5 is an exception case
#odd ===>highest
#evenn ===>lowest
