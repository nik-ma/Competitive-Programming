class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxi=-1
        n=len(nums)
        pre=[nums[0]]
        for i in range(1,n):
            pre.append(pre[-1]+nums[i])
        dicti={}
        pre.insert(0,0)
        nums.append(nums[-1])
        ans=0
        start=0
        # print(pre)
        for i in range(n+1):
            if nums[i] in dicti and dicti[nums[i]]>=start:
                # print(nums[i],ans)
                maxi=max(maxi,ans)
                start=dicti[nums[i]]+1
                dicti[nums[i]]=i

            else:
                ans=pre[i+1]-pre[start]
                dicti[nums[i]]=i
        return maxi
                
                
        