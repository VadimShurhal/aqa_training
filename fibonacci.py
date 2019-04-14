def generateFibonacci(number):
    a,b = 0,1
    for i in range(number):
        yield a
        a,b = b, a + b


def main():
    print(list(generateFibonacci(17)))
    print(list(generateFibonacci(100)))


if __name__ == '__main__':
    main()




