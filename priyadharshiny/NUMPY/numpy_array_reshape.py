import numpy as np

orginal_array = np.array([1,2,3,4,5,6])
print(orginal_array)
print(orginal_array.shape)

print()

reshaped_array = orginal_array.reshape(2,3)
print(reshaped_array)
print(reshaped_array.shape)

print()

reshaped_three_d = orginal_array.reshape(2,1,3)
print(reshaped_three_d)
print(reshaped_three_d.shape)

print()

invalid_reshap = orginal_array.reshape(4,2)
print(invalid_reshap)

auto_reshape = orginal_array.reshape(2,-1)
print(auto_reshape)
print(auto_reshape.shape)