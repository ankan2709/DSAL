
def numDecodingsDP(s: str) -> int:
    memo = [None] * 100

    def solve(i, s, n):
        if memo[i] is not None:
            return memo[i]

        if i == n:
            memo[i] = 1
            return memo[i]  # one valid split done

        if s[i] == '0':
            memo[i] = 0
            return memo[i]  # not possible to split
        
            
        result = solve(i+1, s, n)

        if i+1 < n:
            if s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6): 
                result+= solve(i+2, s, n)

        memo[i] = result
        return memo[i]

    n = len(s)
    return solve(0, s, n)

s = "12"
print(numDecodingsDP(s))



def numDecodings(s: str) -> int:

    def solve(i, s, n):

        if i == n:
            return 1  # one valid split done

        if s[i] == '0':
            return 0  # not possible to split
            
        i_th_char_only = solve(i+1, s, n)
        i_th_plus_1_char = 0

        if i+1 < n:
            if s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6): 
                i_th_plus_1_char = solve(i+2, s, n)

        return i_th_char_only + i_th_plus_1_char

    n = len(s)
    return solve(0, s, n)

# s = "12"


class Solution {
public:
    int n;
    
    int solve(int i, vector<int>& coins, int amount) {
        
        if(amount == 0)
            return t[i][amount] = 1;
        
        if(i == n || amount < 0)
            return 0;
        
        if(coins[i] > amount)
            return solve(i+1, coins, amount);
        
        int take = solve(i, coins, amount-coins[i]);
        int skip = solve(i+1, coins, amount);
        
        return take+skip;
        
    }
    
    int change(int amount, vector<int>& coins) {
        n = coins.size();
        return solve(0, coins, amount);
    }
};