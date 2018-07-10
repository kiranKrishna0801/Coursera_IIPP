def name_and_age(name, age):
    return name + " is " + str(age) + " years old."


def test(name, age):
    print name_and_age(name, age)
    
test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", 46)
