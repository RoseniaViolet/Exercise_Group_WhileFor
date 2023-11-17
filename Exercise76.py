n = int(input('Enter an integer: '))
if n < 2:
    print("Error: Enter a number greater than or equal to 2.")
if n >= 2:
    factor = 2
    print(f"Prime factorization of {n}:")
    while factor <= n:
        if n % factor == 0:
            print(factor)
            n //= factor
        else:
            factor += 1
