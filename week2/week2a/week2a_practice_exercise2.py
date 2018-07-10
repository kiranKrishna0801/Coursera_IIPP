def set_goodbye():
    """prints the console"""
    global message
    message = "goodbye"
    print message
message = "Hello"
print message
set_goodbye()
print message

message = "Ciao"
print message
set_goodbye()
print message

"""def set_goodbye():
    global message
    message = "Ciao"

message = "Good bye"

print message
set_goodbye()
print message"""