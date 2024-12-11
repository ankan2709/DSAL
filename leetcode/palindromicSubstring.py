def getSubstring(string):
    res = []

    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            res.append(string[i:j])

    return res

def isPalindrome(string):
    return string == string[::-1]


def palindrominSubstring(string):
    res = getSubstring(string)

    number = 0
    for item in res:
        if isPalindrome(item):
            number += 1
    return number

print(palindrominSubstring('abc'))
