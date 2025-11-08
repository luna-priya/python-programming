import matplotlib.pyplot as plt
x_value = [22,25,27,31,33,36]
y_value = [87,90,87,90,87,90]
plt.scatter(x_value,y_value,color = "red",s = 100)
plt.xlabel("Age in years")
plt.ylabel("Weight in kg")
plt.title("Scatter plot of age and weight")
plt.show()