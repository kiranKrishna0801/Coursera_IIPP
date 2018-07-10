def is_leap_year(year):
    return(year%4==0)or(year%100==0)or(year%400==0)
def test(year):
    """Tests the is_leapyear function."""
    if is_leap_year(year):
        print year, "is a leap year."
    else:
        print year, "is not a leap year."

test(2000)
test(1996)
test(1800)
test(2013)
