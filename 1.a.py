

def sum():
    reshima = input("enter num ")
    sum2 = 0
    while(reshima != 'stop'):
        sum2 += int(reshima)
        reshima = input("enter num 3")
    print("the sum is:" + str(sum2))
sum()