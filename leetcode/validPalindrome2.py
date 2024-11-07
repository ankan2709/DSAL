def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True
    

def validPalindrom(s):

    if len(s) < 2:
        return True
    
    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return isPalindrome(s, l+1, r) or isPalindrome(s, l, r-1)
        
        l += 1
        r -= 1

    return True

print(validPalindrom("aba"))
print(validPalindrom("abca"))
print(validPalindrom("abc"))