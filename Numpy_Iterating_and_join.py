import numpy as np
#That iterating
arr=np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arr):
    print(x)

print("***************************")
for x in np.nditer(arr[:2,1:3]):
    print(x)
print("***************************")
# That join
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)

print("***************************")
print(np.vstack((arr1,arr2)))