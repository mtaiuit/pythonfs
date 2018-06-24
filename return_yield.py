"""Python"""
def PrintNumber(x):
    for i in range(x):
        yield i*i
    
print PrintNumber(10)