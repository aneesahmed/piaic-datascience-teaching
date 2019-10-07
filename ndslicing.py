import numpy as np

ndarray = np.array (
                    [
                       [ [111, 112, 113, 114 ], [121, 122, 123, 124] , [131, 132, 133, 134] ],
                       [ [211, 212, 213, 214], [221, 222, 223, 224], [231, 232, 233, 234] ],
                       [ [311, 312, 313, 314], [321, 322, 323, 324], [331, 332, 333, 334] ],
                       [  [411, 412, 413, 414], [421, 422, 423, 424], [431, 432, 433, 434] ]
                    ]
                   )
print(ndarray)
subarray = ndarray[2]
print(" ndim ", ndarray.ndim, "shape ", ndarray.shape)
# use of colon is optional means select all
print( ndarray[2, :1])
print(ndarray[2, 1, 2])
print(ndarray[0:4, 0:3, 0:4])
print(ndarray[0:2, 0:1, 0:1 ])

# remember 4th index is not valid but in python indexes stops at -1 of the index
# students bhion, 4 bhi use kar saktay hayn, kiyon kay 4 kaa matlab hay 4 -1,
# ptyhon may range given number say aik com pay ruk jati hay
# supose shape is (4, 3, 5, 2)
#ndarray[2, 2, 3, 1]


