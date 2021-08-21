import numpy as np
x =np.array([[1,2,3,4,5],
            [4,5,6,12,4],
             [1,23,45,6,7]])
#shape(3,5)
y =np.array([[1,2,3,4,5],
            [4,5,6,12,4],
             [1,23,45,6,7],
             [1,3,3,4,5],
             [1,3,3,4,5]])
#y (5,x) لازم تكون
print(x.shape)
print(x)
print(x.T)
print(x.T.shape)
print(x.reshape(1,15))
print(np.where (x== 4))
print  (np.dot(x,y)) #*array(x*y)