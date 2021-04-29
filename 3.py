

def compress(x):
    count = 1
    newx = ''
    for n in range(len(x)-1):
        if(x[n] == x[n+1]):
            count += 1
        else:
            newx += x[n] + str(count)
            count = 1;
    newx += str(x[len(x)-1]) + str(count)
    return newx

x = input("enter letters: ")
print(str(compress(x)))
