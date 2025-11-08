import matplotlib.pyplot as plt
values = [40,30,15,15]
labels = ["rent","groceries","transport","savings"]
explode = (0.1,0,0,0)
plt.pie(values, label=labels, autopct="%.1f%%", explode=explode)
plt.title("Pie Chart Demo")
plt.show()