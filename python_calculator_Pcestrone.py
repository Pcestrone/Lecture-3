# python calculator Peter Cestrone

def add(x, y):
    z = x + y
    #print("{} + {} = {}".format(x, y, z))
    return z

def subtract(x, y):
    z = x - y
    #print("{} - {} = {}".format(x, y, z))
    return z

def multiply(x,y):
    z = x * y
    #print("{} * {} = {}".format(x, y, z))
    return z

def divide(x,y):
    z = x / y
    #print("{} / {} = {}".format(x, y, z))
    return z

c = input("Enter a letter: ")
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("You entered {}".format(x))
print("You entered {}".format(y))
if c == "a":
    d = add(x, y)
    print("{} + {} = {}".format(x, y, d))
elif c == "s":
    d = subtract(x, y)
    print("{} - {} = {}".format(x, y, d))
elif c == "m":
    d = multiply(x, y)
    print("{} * {} = {}".format(x, y, d))
elif c == "d":
    d = divide(x, y)
    print("{} / {} = {}".format(x, y, d))
else:
    print("Does not recognize".format(c))
print("Finished")
