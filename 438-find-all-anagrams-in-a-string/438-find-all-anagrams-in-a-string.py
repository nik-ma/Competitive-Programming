from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def check(a,b):
            if sorted(a)==sorted(b):
                return True
            return False
        if len(s)<len(p):
            return []
        n=len(s)
        dicti1=Counter()
        ans=[]
        for i in p:
            dicti1[i]+=1
        k=len(p)
        dicti2=Counter()
        # for i in range()
        j=0
        count=k
        flag=0
        for i in range(n):
            dicti2[s[i]]+=1
            if dicti1==dicti2:
                ans.append(i-k+1)
            if i==k-1 or flag==1:
                flag=1
                dicti2[s[j]]-=1
                j+=1
                # count=k
            # print(dicti2)
            
        return ans                
            
            
            
        