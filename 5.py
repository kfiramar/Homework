

def map(x,func):
    for n in range(len(x)):
        x[n] = multi(x[n])
    return x

def printx(x):
    for n in range(len(x)):
        print(x[n])
    return x

def multi(x):
    return x ** 2

x = [5,3,6]
map(x,multi)
printx(x)

