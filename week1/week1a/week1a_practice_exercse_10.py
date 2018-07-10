def point_distance(x0, y0, x1, y1):
    return ((x1-x0)**2+(y1-y0)**2)**(1/2.0)

def test(x0, y0, x1, y1):
    """Tests the point_distance function."""
    
    print "The distance from (" + str(x0) + ", " + str(y0) + ") to",
    print "(" + str(x1) + ", " + str(y1) + ") is",
    print str(point_distance(x0, y0, x1, y1)) + "."

test(2, 2, 5, 6)
test(1, 1, 2, 2)
test(0, 0, 3, 4)
