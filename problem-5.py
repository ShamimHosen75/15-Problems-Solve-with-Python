# find prime number from 1 to 100
def get_primes(start, end):
    out = list()
    if start <= 1:
        start = 2

    sieve = [True] * (end + 1)
    for p in range(start, end + 1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, end + 1, p):
                sieve[i] = False
    return out

print(get_primes(1, 100))