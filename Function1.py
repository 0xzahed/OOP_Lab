def fibonacci(n):
    fib = []
    for i in range(n):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[-1] + fib[-2])
    return fib

n = int(input("Enter the number: "))
Number = fibonacci(n)
print("Fibonacci number:", Number)
