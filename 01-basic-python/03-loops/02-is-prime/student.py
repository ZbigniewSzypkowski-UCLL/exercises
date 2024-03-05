def is_prime(n):
    for i in range(2, n):
        print(f"${n} % {i} = {n % i}")
        if n % i == 0:
            return False
    return n > 1