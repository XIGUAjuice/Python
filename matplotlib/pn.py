import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

temperature = np.linspace(100, 45, num=12)
voltage = [396, 408, 420, 432, 444, 456, 468, 480, 492, 504, 516, 528]

plt.xlabel('温度/℃', fontsize=16)
plt.ylabel('电压/mV', fontsize=16)

# ax = plt.gca()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# ax.spines['left'].set_visible(False)

plt.scatter(temperature[0], voltage[0], color='red')
plt.scatter(temperature[-1], voltage[-1], color='red')

plt.text(temperature[0] - 13, voltage[0] - 3, (temperature[0], voltage[0]), fontsize=12)
plt.text(temperature[-1], voltage[-1], (temperature[-1], voltage[-1]), fontsize=12)

plt.plot(temperature, voltage)
plt.legend()
plt.grid(alpha=0.5)
plt.show()
