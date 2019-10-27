import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)
plt.xlim(-1, 1)
plt.ylim(-1, 1)

circle = plt.Circle((0, 0), 0.25, color='b', alpha=1, fill=False, lw=1)
rect = plt.Rectangle((-0.25, -0.25), 0.5, 0.5, color='y',
                     alpha=1, fill=False, lw=2)

plt.grid()
plt.axhline(y=1, color='k')
plt.axvline(x=1, color='k')
ax.add_patch(circle)
ax.add_patch(rect)
fig.savefig("pic.png", dpi=400)

plt.show()
