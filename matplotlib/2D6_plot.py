from die import Die
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']

die_1 = Die(6)
die_2 = Die(6)

results = [die_1.roll() + die_2.roll() for i in range(5000)]
frequencies = [results.count(i) for i in range(2, 13)]

fig, ax = plt.subplots()
width = 0.35
x_positions = np.array(range(2, 13))
rects1 = ax.bar(x_positions - 5, frequencies, width, color='SkyBlue')

ax.set_title("两个六面骰点数之和模拟")
ax.set_xlabel("点数和")
ax.set_ylabel("出现次数")
ax.set_xticks(x_positions)
# ax.set_xticklabels([i for i in range(3, 13)])

ax.legend()
plt.show()