def happyNo(n):

    myset = set()

    while n not in myset:
        myset.add(n)

        if n == 1:
            return True
        
        else:
            digits = []

            while n > 0:
                digits.append(n % 10)
                n //= 10

            n = sum(digit**2 for digit in digits)
    return False

print(happyNo(19))
print(happyNo(2))