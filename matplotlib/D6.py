from die import Die
import pygal

die_6 = Die(6)
results = [die_6.roll() for i in range(5000)]
frequencies = [results.count(i) for i in range(1, 7)]

hist = pygal.Bar()

hist.title = "掷6面骰5000次的结果"
hist.x_labels = [str(i) for i in range(1, 7)]
hist.x_title = "点数"
hist.y_title = "出现次数"

hist.add('D6', frequencies)

hist.render_to_file("6面骰结果.svg")
