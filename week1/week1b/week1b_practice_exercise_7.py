def print_digits(number):
    """Prints the tens and ones digit of an integer in [0,100)."""
    
    if 0 <= number < 100:
        print "The tens digit is " + str(number // 10) + ",",
        print "and the ones digit is " + str(number % 10) + "."
    else:
        print "Error: Input is not a two-digit number."
        
print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)
