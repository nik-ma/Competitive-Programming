import collections,math
class Solution:
    def minimumScore(self, N: List[int], E: List[List[int]]) -> int:
        n, m = len(N), len(E)
        
        G = collections.defaultdict(list)
        C = collections.defaultdict(set)
        A = N[:]
        degree = [0] * n

        for x, y in E:
            G[x].append(y)
            G[y].append(x)
            degree[x] += 1
            degree[y] += 1
        
        V = 0
        seen = set()
        dq = collections.deque()
        for i in range(n):
            V ^= N[i]
            if degree[i] == 1:
                dq.append(i)
                seen.add(i)
    
        while dq:
            cur = dq.popleft()
            for nxt in G[cur]:
                if nxt not in seen:
                    C[nxt].add(cur)
                    C[nxt] |= C[cur]
                    A[nxt] ^= A[cur]
                degree[nxt] -= 1
                if degree[nxt] == 1:
                    seen.add(nxt)
                    dq.append(nxt)
                    
        ans = math.inf
        for i in range(m - 1):
            for j in range(i + 1, m):
                a, b = E[i]
                if b in C[a]: a, b = b, a 
                
                c, d = E[j]
                if d in C[c]: c, d = d, c
                    
                if c in C[a]:
                    cur = [A[c], A[a]^A[c], V^A[a]]
                elif a in C[c]:
                    cur = [A[a], A[c]^A[a], V^A[c]]
                else:
                    cur = [A[a], A[c], V^A[a]^A[c]]
                ans = min(ans, max(cur) - min(cur))
            
        return ans