def dfs(curr, n):

    if len(curr) == n:
        res.append("".join(curr[:]))
        return

    for letter in "ab":
        curr.append(letter)
        dfs(curr, n)
        curr.pop()


res = []
n = 2
dfs([], n)
print(res)