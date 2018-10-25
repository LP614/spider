def fib(num):
    a, b = 0, 1
    for i in range(num):
        a , b =b, a+b
        yield a
m =fib(20)
for val in m:
    print(val)


