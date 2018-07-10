def name_lookup(first_name):
    """Returns the instructor's last name."""
    
    if first_name == "Joe":
        return "Warren"
    elif first_name == "Scott":
        return "Rixner"
    elif first_name == "John":
        return "Greiner"
    elif first_name == "Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"





def test(first_name):
    
    print name_lookup(first_name)
    
test("Joe")
test("Scott")
test("John")
test("Stephen")
test("Mary")
