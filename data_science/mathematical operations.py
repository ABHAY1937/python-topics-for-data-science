#3*3
import numpy as np
a=np.arange(1,10).reshape(3,3)
b=np.arange(10,19).reshape(3,3)
print(a)
print(b)

# [1 2 3]
# [4 5 6] ======>a
# [7 8 9]
#                +  ===========> c
# [10 11 12]
# [13 14 15]=====>b
# [16 17 18]
#Addition  proceed by =====>element by element addition
c=np.add(a,b)
print(c)

#substract (element by elemnt)
d=np.subtract(b,a)
print(d)

#multiplication
e=np.multiply(a,b)
print(e)

#divide
f=np.divide(b,a)
print(f)

#square ==========> square function
g=np.square(a)
print(g)

#square root
h=np.sqrt(d)
print(h)

#triganometric function (sin cos tan cosec sec)


