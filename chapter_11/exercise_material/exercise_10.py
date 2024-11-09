def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    
    p = 2
    while p * p <= n:
        if primes[p]:
            for (m) in range(p * p, n+1, p):
                primes[m] = False
        p += 1
    result = [prime for prime in range(2, n+1) if primes[prime]]
    return result


def main():
    try:
        n = int(input("Enter the size of the list: "))
    except ValueError as e:
        raise e
    res = sieve(n)
    print(res)

main()