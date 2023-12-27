# Concatination

name = input("Name: ").strip().title() # remove trailing and leading space and make it all capital
print("Hello 1st time, " + name) # you can't do this print("string" + 10)


"""
    Understanding print() docummentation
    print (*objects, sep=' ', end='n', file=sys.stdout)
"""

print("Hello", "2nd time",sep= ". ", end = ", ")
print(name)
# Format string

print (f"Hello 3rd time, {name}")