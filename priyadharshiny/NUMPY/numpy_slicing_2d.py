import numpy as np

table_data_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(table_data_array)
print(table_data_array[0:2,:])
print(table_data_array[1:3,1:3])
print(table_data_array[:,1])
print(table_data_array[0::2,:])
print(table_data_array[-2:,:])
print(table_data_array[:,0:2])