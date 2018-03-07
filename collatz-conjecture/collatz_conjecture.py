def collatz_steps(number):
    if number <= 0:
        raise ValueError("given value is less or equal to zero, need positive number")
    elif number == 1:
        return 0
    elif number % 2: #odd
        return 1 + collatz_steps(3 * number + 1)
    else: #even
        return 1 + collatz_steps(number // 2)
