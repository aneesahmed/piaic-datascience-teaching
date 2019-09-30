import numpy as np
text = "Here are some of the things you’ll find in NumPy:"
l = text.split(" ")
arr = np.array(text.split(" "))
prn = print
prn("testing")
print(arr)
lnth = np.vectorize(len)
print(arr[lnth(arr)<5])
#print(arr[( np.vectorize(len)) (arr) <5]) 
print()
# text1 = "How dare you! You can't do that! Mr. Ashhad focus on the class"
# text1 += "Do you want break? or if you don't want: we can practice."
# print(text1) 

