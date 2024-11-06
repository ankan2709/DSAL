import collections

def isAnagram(string1, checkCount):
    count1 = collections.Counter(string1)
    return count1 == checkCount


def allAnagrams(string, check):
    check_len = len(check)
    curr_string = string[:check_len]
    res = []

    checkCount = collections.Counter(check)

    for right in range(check_len, len(string)+1):
        left = right - check_len
        
        curr_string = string[left:right]

        if isAnagram(curr_string, checkCount):
            res.append(left)

    return res

original = "cbaebabacd"
check = "abc"
print(allAnagrams(original, check))