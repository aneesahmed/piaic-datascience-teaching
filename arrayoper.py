import numpy as np
#arr = np.array([[1,2,3],[4,5,6]])
# arr2 = np.array([2])
# arr3 = arr * arr2
# print(arr3)
arr = np.array([12,-45,67,89,34,-2,-2,6,-7,8])
# print(arr)
# print(arr[[4,3,0,6]])

s = [2,6,]
#print(arr[s]) 
print(np.cumsum(arr))
barr = arr>10
print("barr : ",barr)
print("arr : ",arr)
print(barr.sum())
print(np.sum(barr))    
print(arr.sum())
print(barr.any(), arr.any())
print(barr.all(), arr.all())
np.savez('E:\\Sir Nasir 9-1\\arrays.npz', hasan = barr )
arr2=np.load('arrays.npz')
print(arr2['hasan'])

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9],[10,11,12]])
c = np.concatenate([a,b],axis=1)
print('a :',a)
print('b :',b)
print('c :',c)
print("\n\n",np.vstack([a,b]))

a = np.array([0, 41, 42, 300, 400, 500, 43, 40, 800, 900])
print("split : " , np.split(a,[2,5,7]))