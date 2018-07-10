def is_lunchtime(hour, is_am):
    return (hour == 11 and is_am) or (hour == 12 and not is_am)

def test(hour, is_am):
    """Tests the is_lunchtime function."""
    print hour,
    if is_am:
        print "AM",
    else:
        print "PM",
    if is_lunchtime(hour, is_am):
        print "is lunchtime."
    else:
        print "is not lunchtime."

test(11, True)
test(12, True)
test(11, False)
test(12, False)
test(10, False)
