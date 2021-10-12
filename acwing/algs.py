def power(a, b, p):
    ans = 1
    if b == 0:
        ans = 1 % p
    else:
        while(b):
            if (b & 1):
                ans = a * ans % p
            a = a * a % p
            b >>= 1
    return ans