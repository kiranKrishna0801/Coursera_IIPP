def reset():
    """Reset global count to zero."""
    global count
    count = 0
    
def increment():
    """Increment global count."""
    global count
    count += 1

def decrement():
    """Decrement global count."""
    global count
    count -= 1
    
def print_count():
    """Print global count."""
    print count
    
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()
