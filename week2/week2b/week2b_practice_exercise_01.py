import simplegui 



def print_hello():
    print "hello"
def print_goodbye():
    print "goodbye"

frame = simplegui.create_frame("Hello and Goodbye", 200, 200)
frame.add_button("Hello", print_hello)
frame.add_button("Goodbye", print_goodbye)



frame.start()



print_hello()
print_hello()
print_goodbye()
print_hello()
print_goodbye()

