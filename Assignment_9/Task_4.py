import numpy as np
data = np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Row-wise sum: ",data.sum(axis=1))
print("Column-wise sum: ",data.sum(axis=0))
print("Minimum value: ",data.min())
print("Maximum value: ",data.max())
print("Overall Mean: ",data.mean())