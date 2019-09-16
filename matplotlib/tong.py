import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

voltage = np.array([2.875, 6.075, 9.2, 12.45, 15.9, 19.4, 23.425, 26.925])
magnetic = np.array([38.35, 77.05, 115.25, 155.05, 196.9, 239.35, 288, 330.3])
# voltage_2 = np.array([2.76, 4.31, 5.72, 7.84, 10.31, 12.57])
# current_2 = np.array([24.7, 21.8, 19.2, 15.3, 10.4, 6.3])


def f(x, k, b):
    return k * x + b


k, b = optimize.curve_fit(f, magnetic, voltage)[0]
# k_2, b_2 = optimize.curve_fit(f, current[3:], voltage[3:])[0]

fig, ax = plt.subplots()
ax.set_title("霍尔元件的灵敏度", fontsize=16)
ax.set_xlabel("$B/Gs$", fontsize=16)
ax.set_ylabel("$U_H/mV$", fontsize=16)

ax.scatter(magnetic, voltage, color='red', s=10)
# ax.scatter(current_2, voltage_2, color='red', s=10)

# y = np.linspace(0, 360, num=1000)
x = np.linspace(0, 360, num=1000)
ax.plot(x, k * x + b, color='orange')
# ax.plot(y, k_2 * y + b_2, color='orange', label='等效电路外特性')

ax.set_xlim(0)
# ax.set_ylim(14, 16)
# ax.set_aspect('equal')
ax.text(220, 12, "$U_H={k:.2}B{U:.2}$".format(k=k, U=b), fontsize=12)
# ax.legend()


plt.savefig("霍尔元件的灵敏度.png", dpi=500)
# plt.show()
