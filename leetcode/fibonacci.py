memo = [None] * 100

def fibonacci(n):
    if memo[n] is not None:
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]
    
# print(fibonacci(30))


dp = [0, 1]
def fiboDPbottomUp(n):
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])

    return dp[-1]
print(fiboDPbottomUp(5))