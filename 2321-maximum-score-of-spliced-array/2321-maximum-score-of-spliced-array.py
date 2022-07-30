from heapq import heappop, heappush

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        if n == 1:
            return max(nums1[0], nums2[0])
        
        for i in range(1, n):
            nums1[i] += nums1[i-1]
            nums2[i] += nums2[i-1]
        
        ans = 0
        for A, B in [[nums1, nums2], [nums2, nums1]]:
            ans = max(ans, A[-1])
            heap = [0]
            for j in range(n):
                curr = A[-1] - A[j] + B[j] - heap[0]
                ans = max(ans, curr)
                heappush(heap, B[j] - A[j])
        return ans
            