def reverseInteger(x):

    parsed = 0
    sign_neg = x < 0

    x = abs(x)

    while x:
        rem = x % 10
        parsed = parsed * 10 + rem
        x //= 10

    return parsed * -1 if sign_neg else parsed

x = 123
print(reverseInteger(x))

x = -123
print(reverseInteger(x))