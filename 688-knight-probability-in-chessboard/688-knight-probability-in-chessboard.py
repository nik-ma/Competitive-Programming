class Solution:
    def knightProbability(self, N, K, r, c):
        moves = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
        @cache
        def dfs(k,x,y,P):
            p = 0
            if 0 <= x < N and 0 <= y < N:
                if k < K:
                    for dx,dy in moves:
                        p += dfs(k + 1, x + dx, y + dy, P / len(moves))
                else:
                    p = P

            return p

        return dfs(0,r,c,1.0)
        