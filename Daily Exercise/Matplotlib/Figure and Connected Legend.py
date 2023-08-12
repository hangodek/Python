import matplotlib.pyplot as plt
import numpy as np

fig, value = plt.subplots(1, 2, figsize = (10, 6))

year = np.array([1, 2, 3, 4, 5])
console_a = np.array([5.2, 6.5, 4.8, 7.3, 8.1])
console_b = np.array([3.8, 4.2, 5.0, 6.8, 7.5])

line1, = value[0].plot(year, console_a, "o:r", label = "Plot 1")
value[0].set_title("Plot 1")
value[0].set_xlabel("X - Axis")
value[0].set_ylabel("Y - Axis")

line2, = value[1].plot(year, console_b, "o:b", label = "Plot 2")
value[1].set_title("Plot 2")
value[1].set_xlabel("X - Axis")
value[1].set_ylabel("Y - Axis")

lines = [line1, line2]
labels = [line.get_label() for line in lines]
fig.legend(lines, labels)

plt.tight_layout()
plt.show()