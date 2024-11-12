import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 5, 100)
y = 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, color="blue",
                linewidth=2,
                linestyle='-',
                label=r'$Y(x) = \frac{5 \cdot \cos(10x) \cdot \sin(3x)}{\sqrt{x}}$')

plt.title("Графік функції Y(x)", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("Y(x)", fontsize=12)

plt.legend(loc="upper right")

plt.grid(True)
plt.show()
