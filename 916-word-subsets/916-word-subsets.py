from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def isSubset(s,ct2):
            ct=Counter(s)
            # ct2=Counter(t)
            for i in ct2:
                if ct[i]<ct2[i]:
                    return False
            return True
            
        ans=[]
        ct2=Counter()
        for i in words2:
            pt=Counter(i)
            for j in pt:
                if ct2[j]<pt[j]:
                    ct2[j]=pt[j]
        for i in words1:
            if isSubset(i,ct2):
                ans.append(i)
        return ans