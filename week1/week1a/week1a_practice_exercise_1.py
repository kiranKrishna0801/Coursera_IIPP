def miles_to_feet(miles):
    """Returns the number of feet in the given number of miles."""
    
    return miles * 5280

def test(miles):
    print str(miles) + " miles equals",
    print str(miles_to_feet(miles)) + " feet."
test(13)
test(57)
test(87.2)