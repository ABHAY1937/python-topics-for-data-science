#4*4 in 2d
import numpy as np
a=np.arange(1,17).reshape(4,4)
print(a)
#  0   1   2  3
# [ 1  2  3  4]  0
# [ 5  6  7  8]  1
# [ 9 10 11 12]  2
# [13 14 15 16]  3
#[row,columns]
print(a[:2,:3]) #row=0,1 #column=0,1,2
#[1 2 3]
#[5 6 7]

print(a[:3,:3])

print(a[1:4,:3])

print(a[2:4,1:4])
print(a[:,2:4])
print(a[1:,:])
print(a[1:4:2,1:])
print(a[:,1:4:2])
print(a[2::2,1::2])

#zeroth column of data
print(a[:,:1]) #or
print(a[:,0])


#zeroth row of data
print(a[0,:])
