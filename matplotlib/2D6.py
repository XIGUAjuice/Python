from die import Die
import pygal

die_1 = Die(6)
die_2 = Die(6)

results = [die_1.roll() * die_2.roll() for i in range(5000)]
frequencies = [results.count(i) for i in range(1, 37)]

hist = pygal.Bar()

hist.title = "投掷5000次的统计结果"
hist.x_labels = [str(i) for i in range(1, 37)]
hist.x_title = "点数和"
hist.y_title = "出现次数"

hist.add('D6 * D6', frequencies)

hist.render()
