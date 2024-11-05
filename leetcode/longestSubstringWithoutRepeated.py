def longestSubstringWithoutRepeated(string):
    myset = set()

    l = 0
    r = 0
    maxSoFar = 0
    while r < len(string) - 1:
        while string[r] in myset:
            myset.remove(string[l])
            l += 1
        myset.add(string[r])
        length = (r - 1) + 1
        maxSoFar = max(maxSoFar, length)
        r += 1

    return maxSoFar

print(longestSubstringWithoutRepeated('ABCDBEA'))


        