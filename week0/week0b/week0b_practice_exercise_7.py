present_value = 1000
annual_rate = 7
years = 10
future_value = present_value * (1 + 0.01 * annual_rate) ** years



print "The future value of $" + str(present_value) + " in " + str(years),
print "years at an annual rate of " + str(annual_rate) + "% is $" + str(future_value) + "."