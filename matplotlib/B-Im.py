import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['grid.linestyle'] = (2, 2)

i_m = np.linspace(50, 400, num=8)
b = np.array([38.35, 77.05, 115.25, 155.05, 196.9, 239.35, 288, 330.3])

insert_i_m = np.linspace(50, 400, num=300)
func_insert = interp1d(i_m, b, kind='cubic')
insert_b = func_insert(insert_i_m)

fig, ax = plt.subplots()
ax.set_title("$B-I_M$"+"磁化曲线", fontsize=16)
ax.set_xlabel("励磁电流"+"$I/mA$", fontsize=16)
ax.set_ylabel("磁感应强度"+"$B/Gs$", fontsize=16)


ax.scatter(i_m, b, color='red', s=10)
ax.plot(insert_i_m, insert_b, color='orange')
ax.set_ylim(0)
ax.set_xlim(0)
ax.set_aspect("equal")


plt.savefig("磁化曲线.png", dpi=500)
plt.show()
