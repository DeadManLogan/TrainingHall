# Use None as default in mutable objects
def fib(series=None):
    if series is None:
        series = [1, 1]

    series.append(series[-1] + series[-2])
    return series

fib1 = fib()
print(fib1)
fib1 = fib(fib1)
print(fib1)

fib2 = fib()
print(fib2)
