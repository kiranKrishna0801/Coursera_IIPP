def circle_circumference(radius):
    return 2 * 3.14 * radius

def test(radius):
    print "A circle with a radius of " + str(radius),
    print "inches has a circumference of",
    print str(circle_circumference(radius)) + " inches."

test(8)
test(3)
test(12.9)
