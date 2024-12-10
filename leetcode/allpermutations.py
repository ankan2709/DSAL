def solve(temp, letters):

    if len(temp) == n:
        res.append("".join(temp))
        return 
    
    for i in range(n):
        if letters[i] not in myset:
            temp.append(letters[i])
            myset.add(letters[i])
            
            solve(temp, letters)

            temp.pop()
            myset.remove(letters[i])

letters = list('abc')
res = []
myset = set()
n = len(letters)
solve([], letters)
print(res)