def reverseBits(n):

    res = 0

    for _ in range(32):
        rightmost_bit = n & 1
        res = (res << 1) | rightmost_bit

        n >>= 1

    return res

