import time


def is_prime(n):
    """ Checks for prime nos within a range """
    # Get start time
    start_time = time.time()

    primes = []
    for num in range(0, n + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)

    # get execution time before function returns
    time_taken = time.time() - start_time

    return primes
