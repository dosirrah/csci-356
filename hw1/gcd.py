def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


if __name__ == "__main__":
    print(gcd(0,20))   # outputs 20. works.
    print(gcd(-1,2))      # outputs 1.  works.
    print(gcd(2, -1))    # WRONG! This prints -1 which is incorrect.  It should be 1.
    print(gcd(-20, -15))     # WRONG! This prints -5 which is incorrect.  It should be 5.
    print(gcd(0, 5))  # outputs 5.  works.
    print(gcd(5, 0))  # WRONG. Fails with an exception.
