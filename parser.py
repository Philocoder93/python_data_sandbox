from matplotlib import pyplot
inputname = '../human-freedom-index.csv.13'

page = open(inputname, 'r')

split_data = []

for line in page:
    if '#' != line[0]:
        split_line = line[:-9].split(',')
        split_data.append(split_line)


filtered_data = filter(lambda x: len(x) > 3, split_data)

x_points = []
y_points = []
counter = 0

for point  in filtered_data:
    print(point)
    if counter == 0:
        counter += 1
        continue
    try:
        floated_x = (float)(point[2])
        floated_y = (float)(point[3])
    except:
        continue
    x_points.append(floated_x)
    y_points.append(floated_y)


print(x_points)
print(y_points)

pyplot.scatter(x_points, y_points, s=1, c='blue')



#x_points = [x for x in range(10)]

#y_points = [x*2 for x in range(10)]

#pyplot.plot(x_points, y_points, color='green', linestyle='solid')

pyplot.show()
