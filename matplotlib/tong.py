import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

temperature = np.array([30, 35, 40, 45, 50, 55, 60, 65])
resistance = np.array([56.872, 57.732, 58.787, 59.652, 60.473, 61.344, 62.218, 63.046])


def f(x, k, b):
    return k * x + b


k, b = optimize.curve_fit(f, temperature, resistance)[0]

fig, ax = plt.subplots()
ax.set_title("铜电阻随温度关系变化图", fontsize=16)
ax.set_xlabel("温度/℃", fontsize=16)
ax.set_ylabel("电阻/Ω", fontsize=16)

ax.scatter(temperature, resistance, color='red', s=10)

x = np.linspace(0, 100, num=1000)
ax.plot(x, k * x + b, color='orange')

ax.set_xlim(0)
ax.set_ylim(b - 1)
ax.text(60, 60, r"$R=0.176T+51.631$", fontsize=12)

plt.savefig("铜电阻.png", dpi=500)
