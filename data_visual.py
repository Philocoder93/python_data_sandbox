from matplotlib import pyplot

x_points = [x for x in range(10)]

y_points = [x*2 for x in range(10)]

#pyplot.plot(x_points, y_points, color='green', linestyle='solid')
pyplot.bar(x_points, y_points)
pyplot.show()
