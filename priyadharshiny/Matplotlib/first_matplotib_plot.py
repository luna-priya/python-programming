import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [2,4,6,8,10]

plt.plot(x_values,y_values,'ro')
#plt.show()
plt.xlabel("X Axis Value")
plt.ylabel("Y Axis Value")
plt.title("My first Matplotlib plot")
plt.plot(x_values,y_values, color = "red", marker = "o")
plt.grid()
plt.show()