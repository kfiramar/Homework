

def IDcheck(x):
    xcell = x[0]
    oneortwo = 1
    number = ''
    sum = 0
    count = 1

    while(str(xcell) != '-'):
        if(oneortwo * int(xcell) > 9):
            number = str(oneortwo * int(xcell))
            sum += int(number[0]) + int(number[1])
        else:
            sum += oneortwo * int(xcell)

        if(oneortwo == 1):
            oneortwo = 2
        else:
            oneortwo = 1
        xcell = x[count]
        count += 1
    if(10 - sum % 10 == int(x[len(x) - 1])):
        return ("this ID is valid")
    else:
        return("this ID is NOT valid")



x = '54370042-1'
print(str(IDcheck(x)))
