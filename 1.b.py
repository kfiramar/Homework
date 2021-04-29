

def sumall():
    x = input("enter numbers with , ")
    reshima = x.split(',')
    sum2 = 0
    for i in reshima:
        sum2 += int(i)

    print("the sum is:" + str(sum2))
sumall()