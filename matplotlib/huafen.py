import random
import matplotlib.pyplot as plt


class Random_Walk():
    def __init__(self, num=5000):
        self.num = num
        self.x = [0]
        self.y = [0]

    def get_step(self):
        direction = random.choice([-1, 1])
        x_distance = random.choice(list(range(0, 9)))
        y_distance = random.choice(list(range(0, 9)))
        self.x_step = direction * x_distance
        self.y_step = direction * y_distance

    def fill_walk(self):
        while(len(self.x) < self.num):
            self.get_step()

            if self.x_step == 0 and self.y_step == 0:
                continue

            x_next = self.x[-1] + self.x_step
            y_next = self.y[-1] + self.y_step

            self.x.append(x_next)
            self.y.append(y_next)


random.seed()

rm = Random_Walk(5000)
rm.fill_walk()

plt.figure(figsize=(15, 11))
plt.plot(rm.x, rm.y)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
