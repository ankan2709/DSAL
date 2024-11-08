import collections

def groupAnagramsEff(strs):
    res = collections.defaultdict(list)

    for word in strs:
        count = [0]*26
        for char in word:
            count[ord(char) - ord("a")] += 1
        res[tuple(count)].append(word)

    return list(res.values())

def groupAnagrams(strings):
    # time complexity = O(nlog(m))
    res = collections.defaultdict(list)
    for word in strings:
        sorted_word = "".join(sorted(word))
        res[sorted_word].append(word)

    return list(res.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))