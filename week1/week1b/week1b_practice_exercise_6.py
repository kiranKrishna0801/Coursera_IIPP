def name_and_age(name, age):
    """Returns a string stating the person's age."""
    if age >= 0:
        return name + " is " + str(age) + " years old."
    else:
        return "Error: Invalid age"
           
def test(name, age):
    print name_and_age(name, age)
    
test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", -46)

