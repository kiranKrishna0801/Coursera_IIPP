def pig_latin(word):
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    

    if (first_letter == "a" or first_letter == "e" or first_letter == "i" or
        first_letter == "o" or first_letter == "u"):
        return word + "way"
    else:
        return rest_of_word + first_letter + "ay"



def test(word):
    """Tests the pig_latin function."""
    
    print pig_latin(word)
    
test("pig")
test("owl")
test("python")