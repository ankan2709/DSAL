def longestSubstring(string):
    charset = set()

    left = 0
    max_length = 0

    for right in range(len(string)):
        while string[right] in charset:
            charset.remove(string[left])
            left += 1

        charset.add(string[right])
        max_length = max(max_length, right - left + 1)
    return max_length


print(longestSubstring("abccabcabcc"))
print(longestSubstring("aaaabaaa"))