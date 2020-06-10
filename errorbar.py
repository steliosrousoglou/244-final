import numpy as np
import matplotlib.pyplot as plt

def error_bars (l):
	return [min(l), max(l)]

data = np.array([[1, 1, 1, 1] \
,[0.999, 0.977, 0.934, 0.984] \
,[0.9, 0.92, 0.93, 0.95] \
,[0.9, 0.89, 0.94, 0.91] \
,[0.88, 0.89, 0.91, 0.89]])

points = np.array([np.mean(p) for p in data])
bars = np.transpose([error_bars(p) for p in data])
bars[0][:] -= points
bars[1][:] = points - bars[1][:]

print(bars)

plt.errorbar([0, 5, 10, 15, 20], points, bars, marker="o", markersize=10, \
	linewidth=1, fillstyle="none", color="red", capsize=10)
plt.ylim(0.8, 1.1)
plt.xticks([0, 5, 10, 15, 20])
plt.show()