import numpy as np
a=np.array([1,23,4,7,5,8,4,6])
print(a)
for i in a:
    print(i)
#2D array itteration ===========>  2loop
import numpy as np
b=np.arange(16).reshape(4,4)
print(b)
for i in b:
    for j in i:
        print(j)
#3d array ====> 3 loop for exicute
import numpy as np
# c=p.array([[[1,2,3],[4,5,6],[7,8,9]]]).
# print(c)

#where function   ==== to find the element present or not using this function
print(np.where(a==4))
x=np.where(b==4)
print(x)
print(np.where(b>5))
print(np.where(b%2==1))
