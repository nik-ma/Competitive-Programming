class Solution:
    def numFactoredBinaryTrees(self, A):
        A.sort()
        dp = collections.defaultdict(int)
        for i, v in enumerate(A):
            dp[v] = 1 + sum(dp[A[j]]*dp[v/A[j]] for j in range(i) if not v%A[j])
        return sum(dp.values()) % 1000000007