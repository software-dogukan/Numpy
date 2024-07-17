import numpy as np
arr=np.array([1,6,4,7,3,9,8,0])
print(np.sort(arr))
print("*****************************")
arr_bool=[True,False,False,True,True,False,False,True]
print(arr[arr_bool])
print("*******************************")
arr_bool=[]
for x in arr:
    if x>5:
        arr_bool.append(True)
    else:
        arr_bool.append(False)
new_arr=arr[arr_bool]
print(new_arr)
print("******************************")
newarr=arr<5
new_arr=arr[newarr]
print(np.sort(new_arr))



