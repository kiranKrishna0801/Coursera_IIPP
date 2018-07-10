import random
def powerball():
    """Prints Powerball lottery numbers."""
    
    print "Today's numbers are " + str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ",",
    print str(random.randrange(1, 60)) + ", and",
    print str(random.randrange(1, 60)) + ". The Powerball number is",
    print str(random.randrange(1, 36)) + "."

powerball()
powerball()
powerball()
