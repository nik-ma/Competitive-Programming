class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=[[] for i in range(n)]
        for i in flights:
            graph[i[0]].append([i[1],i[2]])
        @cache
        def solve(node,k):
            if node==dst and k>=0:
                return 0
            if k<0:
                return float('inf')
            mini=float('inf')
            for i in graph[node]:
                mini=min(mini,i[1]+solve(i[0],k-1))
            return mini
        ans=solve(src,k+1)
        return -1 if ans==float('inf') else ans
                