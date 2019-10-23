import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)

plt.title("Lab #3.5")

ax = plt.subplot(1, 1, 1)
plt.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
x = np.linspace(-10, 20, 500)
ax.plot(x, 6 * x - 2, "r")
ax.plot(x, -x + 12, "g")
# x = 2 y = 10
ax.legend(["$6x-2$", "$-x+12$"])
ax.annotate("$c = (2,10)$", xy=(2, 10), xytext=(-2, 30), fontsize=18,
            arrowprops=dict(facecolor="red", arrowstyle="simple"))

plt.show()
