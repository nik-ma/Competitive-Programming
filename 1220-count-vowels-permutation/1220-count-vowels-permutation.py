class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MODULO = 10**9 + 7
        dp = [1] * 5
        for _ in range(1, n):
            a, e, i, o, u = dp
            dp[0] = (e + i + u) % MODULO
            dp[1] = (a + i) % MODULO
            dp[2] = (e + o) % MODULO
            dp[3] = i % MODULO
            dp[4] = (i + o) % MODULO
            
        return sum(dp) % MODULO
        