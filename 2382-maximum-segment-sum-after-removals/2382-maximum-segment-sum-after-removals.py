from sortedcontainers import SortedList
class Solution: 
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        sl = SortedList([-1, n])
        prefix = list(accumulate(nums, initial=0))
        mp = {-1 : n}
        pq = [(-prefix[-1], -1, n)]
        
        ans = []
        for q in removeQueries: 
            sl.add(q)
            i = sl.bisect_left(q)
            lo = sl[i-1]
            hi = sl[i+1]
            mp[lo] = q
            mp[q] = hi 
            heappush(pq, (-(prefix[q]-prefix[lo+1]), lo, q))
            heappush(pq, (-(prefix[hi]-prefix[q+1]), q, hi))
            
            while mp[pq[0][1]] != pq[0][2]: heappop(pq)
            ans.append(-pq[0][0])
        return ans 