import matplotlib.pyplot as plt
departments = ["IT","Finance","HR"]
salaries = [60000,70000,80000]
plt.bar(departments,salaries,color = ["blue","green","red"],width = 0.5)
plt.title("Average salary by department")
plt.xlabel("Department")
plt.ylabel("Average salary")
plt.show()
plt.bar(departments,salaries,color = "purple")
plt.title("Average salary by department")
plt.xlabel("Department")
plt.ylabel("Average salary")
plt.show()