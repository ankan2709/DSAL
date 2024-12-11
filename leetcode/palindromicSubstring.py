







# # brute force

def isPalidrome(s):
    l = 0
    r = len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def palindrominSubstringIndex(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subString = s[i:j]
            if isPalidrome(subString):
                count += 1
    return count

print(palindrominSubstringIndex('abc'))



