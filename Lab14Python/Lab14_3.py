import numpy as np
import matplotlib.pyplot as plt

print("Population of people in Ukraine for 10 years: ")
x = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006]
y = [47105171, 46787786, 46509355, 46258189, 46053331, 45870741, 45706086, 45593342, 45489648, 45272155, 45167350]

np.array(x)
np.array(y)

fig, ax = plt.subplots()
ax.pie(y, labels = x)
ax.axis("equal")

plt.legend()
plt.show()
