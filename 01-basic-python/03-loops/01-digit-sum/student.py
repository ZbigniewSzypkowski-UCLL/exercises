def last_digit(x):
    return x % 10

def remove_last_digit(x):
    return x // 10

def digit_sum(x):
    tot = 0
    while x > 0:
        tot += last_digit(x)
        x = remove_last_digit(x)
    return tot