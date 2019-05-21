import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams["grid.linestyle"] = (2, 2)   # 网格线密度

cigan = np.array([
    30.16, 27.14, 24.13, 21.11, 18.10, 15.08, 12.06, 9.05, 6.03, 3.02, 1.51,
    0.00, -1.51, -3.01, -6.03, -9.04, -12.06, -15.08, -18.10, -21.11, -24.13,
    -27.14, -30.16
])

cizu_down = np.array([
    1860.47, 1860.47, 1869.16, 1869.16, 1877.93, 1913.88, 1951.22, 1990.05,
    2030.46, 2072.54, 2083.33, 2105.26, 2094.24, 2072.54, 2040.82, 2000.00,
    1960.78, 1923.08, 1886.80, 1869.16, 1869.16, 1869.16, 1860.46
])

cizu_up = np.array([
    1851.85, 1860.46, 1860.46, 1869.16, 1886.79, 1923.08, 1960.78, 2000.00,
    2040.82, 2072.54, 2094.24, 2094.24, 2072.54, 2051.28, 2010.05, 1970.44,
    1932.37, 1895.73, 1869.16, 1869.16, 1861.85, 1851.85, 1851.85
])

new_x = np.linspace(cigan.min(), cigan.max(), 300)

func_down = interp1d(cigan, cizu_down, kind='cubic')
func_up = interp1d(cigan, cizu_up, kind='cubic')
new_y1 = func_down(new_x)
new_y2 = func_up(new_x)

plt.plot(new_x, new_y1, color='green', label='减小磁场')
plt.plot(new_x, new_y2, color='red', label='增大磁场')
plt.xlabel('磁感应强度/高斯')
plt.ylabel('磁阻/Ω')
plt.legend()
plt.grid()
plt.savefig('巨磁阻.png', dpi=500)
