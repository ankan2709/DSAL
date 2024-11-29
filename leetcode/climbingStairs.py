memo = [None] * 46

def solve(n):
    if memo[n] is not None:
        return memo[n]
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    one_step = solve(n-1)
    two_step = solve(n-2)
    memo[n] = one_step + two_step
    return memo[n]

print(solve(4))