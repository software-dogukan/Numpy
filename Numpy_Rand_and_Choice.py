import numpy as np
arr=np.random.randint(100)
print(arr)
print("*******************************")
arr=np.random.randint(100,size=(2,5))
print(arr)
print("********************************")
arr=np.random.choice([1,3,5,7])
print(arr)
print("********************************")
arr=np.random.choice([1,3,5,7,8,6,4,2,0,1],size=(2,3))
print(arr)