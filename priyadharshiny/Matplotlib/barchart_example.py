import matplotlib.pyplot as plt
categories = ["math", "science", "english", "history", "geography"]
scores = [88, 92, 80, 75, 85]

plt.bar(categories,scores ,color = "green")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.title("Exam scores by subjects")

plt.grid()
plt.show()