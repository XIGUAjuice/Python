from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    """ 一个生成随机漫步数据的类 """

    def __init__(self, num_points=5000):
        """ 初始化属性 """
        self.num_points = num_points

        # 从（0,0）开始
        self.x = [0]
        self.y = [0]

    def fill_walk(self):
        """ 计算随机漫步需要的点 """

        while len(self.x) < self.num_points:
            x_direction = choice([-1, 1])
            y_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            y_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x[-1] + x_step
            next_y = self.y[-1] + y_step

            self.x.append(next_x)
            self.y.append(next_y)


rm = RandomWalk()
rm.fill_walk()
point_numbers = list(range(rm.num_points))
plt.scatter(rm.x, rm.y, s=10, c=point_numbers, cmap=plt.cm.gist_rainbow)
plt.scatter(0, 0, color='green', s=100)
plt.scatter(rm.x[-1], rm.y[-1], color='red', s=100)
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)
plt.grid()
plt.show()
