import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(newarr)
print("*************************")
print(np.where(arr%2==0))
print("*************************")
print(np.searchsorted(arr,4))
