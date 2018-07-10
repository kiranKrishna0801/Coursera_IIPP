def circle_area(radius):
    return 3.14*radius**2
def test(radius):
    print "A circle with a radius of " + str(radius),
    print "inches has an area of",
    print str(circle_area(radius)) + " square inches."

test(8)
test(3)
test(12.9)
