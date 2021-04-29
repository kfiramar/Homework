cache = dict()
def Decorator(num1, num2):
    s = str(num1)+str(num2)
    if(s in cache.keys()):
        return cache.get(s)
    sum = num1 + num2
    cache.update({s : sum})
    return sum

print(Decorator(2,43))
print(Decorator(2,43))