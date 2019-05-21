import csv
import matplotlib.pyplot as plt
import numpy as np

filename = "Motor_Vehicle_Crashes_-_Vehicle_Information__Three_Year_Window.csv"
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    crash_dic = {}
    for row in reader:
        if row[4] in crash_dic:
            crash_dic[row[4]] += 1
        else:
            crash_dic[row[4]] = 1


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots()
n = len(crash_dic)
x = np.linspace(5, 200, n)

ax.bar(x, crash_dic.values())
ax.set_xticks(x)
ax.set_xticklabels(crash_dic.keys(), rotation=20)

plt.show()

