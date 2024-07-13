import numpy as np
arr=np.array([1,2,3,4,5])
copy_arr=arr.copy()
arr[0]=8
print(arr)
print(copy_arr)
########################################################
view_arr=arr.view()
view_arr[0]=15
print(arr)
print(view_arr)
#########################################################