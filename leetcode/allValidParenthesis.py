def isvalid(curr):
    stack = []
    closeToOpen = {')':'(', '}':'{', ']':'['}
    
    for i in range(len(curr)):
        if curr[i] in {'(','{','['}:
            stack.append(curr[i])
        else:
            if stack and stack[-1] == closeToOpen[curr[i]]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


res = []
def solve(curr, n):

    if len(curr) == 2*n:
        if isvalid(curr):
            res.append("".join(curr[:]))
            return
        else:
            return False
    curr.append("(")
    solve(curr, n)
    curr.pop()
    curr.append(")")
    solve(curr, n)
    curr.pop()
n = 2
solve([], n)
print(res)