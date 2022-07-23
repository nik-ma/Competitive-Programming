class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        n=len(rolls)
        ans=1
        i=0
        st=set()
        while i<n:
            st.add(rolls[i])
            if len(st)==k:
                ans+=1
                st=set()
            i+=1
        return ans