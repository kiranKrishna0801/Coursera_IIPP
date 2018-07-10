def point_distance(x0, y0, x1, y1):
    
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
def triangle_area(x0, y0, x1, y1, x2, y2):
    
    a = point_distance(x0, y0, x1, y1)
    b = point_distance(x0, y0, x2, y2)
    c = point_distance(x1, y1, x2, y2)
    
    
    s = (a + b + c) / 2
    
    
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
def test(x0, y0, x1, y1, x2, y2):
    """Tests the triangle_area function."""
    
    print "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
    print "(" + str(x1) + "," + str(y1) + "), and",
    print "(" + str(x2) + "," + str(y2) + ") has an area of",
    print str(triangle_area(x0, y0, x1, y1, x2, y2)) + "."

test(0, 0, 3, 4, 1, 1)
test(-2, 4, 1, 6, 2, 1)
test(10, 0, 0, 0, 0, 10)