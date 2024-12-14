def function(x):
    fib_numbers = {0: 0, 1: 1}

    if x in fib_numbers:
        return fib_numbers[x]

    for i in range(2, x + 1):
        next_fib = fib_numbers[i - 1] + fib_numbers[i - 2]
        fib_numbers[i] = next_fib

    return fib_numbers[x]