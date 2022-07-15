from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dicti=Counter()
        for i in time:
            dicti[i]+=1
        t2=[60*i for i in range(100)]
        ans=0
        for i in time:
            for j in t2:
                if j-i in dicti:
                    if i==j-i:
                        ans+=dicti[j-i]-1
                    else:
                        ans+=dicti[j-i]
                    print(i,j-i)
        # print(ans)
        return ans//2
                        