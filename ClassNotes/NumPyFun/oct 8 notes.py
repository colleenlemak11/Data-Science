import numpy as np
 
x = list(range(10))
print(x)
 
# make a numpy ndarray
x = np.array(x)
print(x)
print(type(x))
 
# 2D
x = [[1, 2, 3], [4, 5, 6]]
print(x)
x = np.array(x)
print(x)
print(x.ndim)
print(x.shape) # rows x cols
print(x.dtype)
 
# convert x to be an array of floats
x_floats = x.astype(np.float)
print(x_floats)
print(x_floats.dtype)
 
x = np.arange(10)
print(x)
 
x = np.arange(2, 12, 2) # start, stop, step
print(x)
 
x = np.ones((4, 5))
print(x)
 
x = np.zeros(10)
print(x)
 
x = np.full(10, 5.5)
print(x)
 
# indexing
x = np.ones((4, 5))
print(x[0][0], x[0, 0])
 
# vectorization
x = list(range(10))
y = list(range(10, 20))
print(x)
print(y)
z = []
for i in range(len(x)):
   z.append(x[i] + y[i])
print(z)
print(x + y)
 
# solve again using numpy arrays and vectorized +
x = np.arange(10)
y = np.arange(10, 20)
print(x)
print(y)
z = x + y
print(z)
 
# relational operators
m_names = np.array(["Mary", "Michael", "Margaret", "Mary", "Marcus", "Molly"])
m_ages = np.array([   28,     72,        12,         34,     40,       68])
# Boolean array
marys = m_names == "Mary"
print(marys)
# we can do Boolean indexing with a Boolean array
mary_ages = m_ages[marys]
print(mary_ages)
 
# and, or, not are vectorized as &, |, ~ (boolean array) or np.logical_not() for integer arrays
 
# broadcasting
x = np.arange(10)
print(x)
# multiply all elements in x by 2
x *= np.array([2])
print(x)
 
# advanced assignment
from numpy.random import randn
rand_data = randn(3, 4)
print(rand_data)
rand_data[0][2] = 100.0
print(rand_data)
 
# Boolean array for negative values
negatives = rand_data < 0
print(negatives)
# set the negative values to b 0
rand_data[negatives] = 0 # batch assignment
print(rand_data)
 
# slicing
x = list(range(10))
print(x)
slice_x = x[3:7] # copy
print(slice_x)
slice_x[0] = 100
print(slice_x)
print(x)
 
x = np.arange(10)
print(x)
slice_x = x[3:7] # view, a copy!!
print(slice_x)
slice_x[0] = 100
print(slice_x)
print(x)
 
x = np.arange(10)
print(x)
slice_x = x[3:7].copy() # copy
print(slice_x)
slice_x[0] = 100
print(slice_x)
print(x)
 
# scalars can be broadcast to slices
x[2:5] = 500
print(x)
 
# reshaping
x = np.arange(10)
print(x.shape)
x = x.reshape(5, 2)
print(x.shape)
print(x)
 
# transposing
x = x.T
print(x)
 
# ndarray functions
# unary ufuncs
x = np.arange(10)
print(x)
print(np.sqrt(x))
 
# binary ufuncs
y = np.arange(10, 20)
print(y)
print(np.add(x, y))
print(np.power(x, np.full(10, 2.0)))
print(np.power(x, 2.0))