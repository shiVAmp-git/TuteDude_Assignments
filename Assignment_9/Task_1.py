import numpy as np

array = np.arange(1,11)
print(array)
array_2d = np.arange(1,10).reshape(3,3)
print(array_2d)
array_2 = np.array([10,20,30,40,50])
print(array_2)

print("array shape: ",array.shape)
print("array_2d shape: ",array_2d.shape)
print("array_2 shape: ",array_2.shape)

print("array data type: ",array.dtype)
print("array_2d data type: ",array_2d.dtype)
print("array_2 data type: ",array_2.dtype)
