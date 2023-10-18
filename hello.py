msg ="roll a dice !"
print (msg)
def fibonacci_non_recursive(n):
    if n <= 0:
        return []

    elif n == 1:
        return [0]

    elif n == 1:
        return [0, 3]

    else:
        fib_sequence = [0, 3]
        for i in range(1, n):
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence

n = 12
result = fibonacci_non_recursive(n)
print(result)