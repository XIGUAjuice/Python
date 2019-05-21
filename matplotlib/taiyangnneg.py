import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

voltage = np.array([
    3.2, 3.19, 3.18, 3.17, 3.16, 3.15, 3.14, 3.12, 3.09, 3.02, 2.65, 2.46,
    2.22, 1.93, 1.71, 1.43, 1.15, 0.88, 0.6
])
current = np.array([
    6.3, 7.9, 16.0, 31.8, 39.5, 52.5, 62.5, 77.8, 102.8, 150.8, 273, 277, 279,
    274, 282, 275, 284, 285, 286
])

voltage_new = np.linspace(voltage.min(), voltage.max(), 500)
func_1 = interp1d(voltage, current, kind='cubic')
current_new = func_1(voltage_new)

fig, axs = plt.subplots(2, 1)

axs[0].plot(voltage_new, current_new)
axs[0].set_xlabel('输出电压/V', fontsize=16)
axs[0].set_ylabel('输出电流/mA', fontsize=16)
axs[0].grid(alpha=0.5)

power_new = np.array([a * b for a, b in zip(voltage_new, current_new)])

axs[1].plot(voltage_new, power_new)
axs[1].set_xlabel('输出电压/V', fontsize=16)
axs[1].set_ylabel('功率/mW', fontsize=16)
axs[1].grid(alpha=0.5)

fig.tight_layout()
plt.show()