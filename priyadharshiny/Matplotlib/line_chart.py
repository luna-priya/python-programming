import matplotlib.pyplot as plt
days = ["mon","tue","wed","thur","fri","sat","sun"]
visits = [250,270,300,280,350,400,420]
plt.plot(days,visits)
plt.title("Website traffic over a week")
plt.xlabel("Day of the week")
plt.ylabel("Number of Visitors")
plt.show()