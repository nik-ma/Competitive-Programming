class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        val=[]
        for i in set(s):
            start=s.index(i)
            end=len(s)-s[::-1].index(i)-1
            val.append([start,end])
        val.sort()
        ans=[[val[0][0],val[0][1]]]
        i=1
        n=len(val)
        # print(ans)
        while i<n:
            if ans[-1][1]>=val[i][0]:
                ans[-1][1]=max(ans[-1][1],val[i][1])
            else:
                ans.append(val[i])
            i+=1
        newans=[]
        # print(ans,val)
        for i in ans:
            newans.append(i[1]-i[0]+1)
        return newans
        
        
            
            
                
                    
        