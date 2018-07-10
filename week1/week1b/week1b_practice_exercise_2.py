def is_cool(name):
    
    
    return (name == "Joe") or (name == "John") or (name == "Stephen")

def test(name):
    """Tests the is_cool function."""
    
    if is_cool(name):
        print name, "is cool."
    else:
        print name, "is not cool."

test("Joe")
test("John")
test("Stephen")
test("Scott")