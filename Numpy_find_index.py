import numpy as np

numbers_list=np.array([[1,2,3,4],[5,6,7,8]])

print(numbers_list[0:,1:3])
print("*************************")
print(numbers_list[:,-3:-1])
print("*************************")
print(numbers_list[:,-3:-1])

numbers_list=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print("*************************")
print(numbers_list[0:1,:,:])
print("*************************")
print(numbers_list[0:1,1:2,:])
print("*************************")
print(numbers_list[0:1,1:2,1:4])


