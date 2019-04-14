def fibonacci(number):
    a,b = 0,1
    for i in range(number):
        yield a
        a,b = b, a + b


print(list(fibonacci(1000)))
