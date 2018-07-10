
x0, y0 = 0, 0
x1, y1 = 3, 4
x2, y2 = 1, 1
a = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
b = ((x0 - x2) ** 2 + (y0 - y2) ** 2) ** 0.5
c = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
print "(" + str(x1) + "," + str(y1) + "), and",
print "(" + str(x2) + "," + str(y2) + ") has an area of " + str(area) + "."
