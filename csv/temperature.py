import csv
import datetime
import matplotlib.pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.datetime.strptime(row[0], "%Y-%m-%d")
            high_temperature = int(row[1])
            low_temperature = int(row[3])
        except ValueError:
            print(date, "missing data!")
        else:
            highs.append(high_temperature)
            dates.append(date)
            lows.append(low_temperature)

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates2, highs2, lows2 = [], [], []
    for row in reader:
        try:
            date = datetime.datetime.strptime(row[0], "%Y-%m-%d")
            high_temperature = int(row[1])
            low_temperature = int(row[3])
        except ValueError:
            print(date, "missing data!")
        else:
            highs2.append(high_temperature)
            dates2.append(date)
            lows2.append(low_temperature)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(1, 2)

ax[0].plot(dates, highs, c='r', label='最高气温')
ax[0].plot(dates, lows, c='b', label='最低气温')
ax[0].fill_between(dates, lows, highs, facecolor='pink', alpha='0.5')

ax[1].plot(dates2, highs2, c='r')
ax[1].plot(dates2, lows2, c='b')
ax[1].fill_between(dates2, lows2, highs2, facecolor='pink', alpha='0.5')

ax[0].set_xlabel("日期")
ax[0].set_ylabel("温度/F")
ax[0].set_title("锡特卡2014年气温折线图")
ax[1].set_title("死亡谷2014年气温折线图")
ax[0].set_yticks(list(range(0, 120, 5)))
ax[1].set_yticks(list(range(0, 120, 5)))

fig.autofmt_xdate()
fig.legend()
fig.tight_layout
plt.tick_params(axis='both', which='major')
plt.show()
