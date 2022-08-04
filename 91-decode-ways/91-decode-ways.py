class Solution:
    def numDecodings(self, s: str) -> int:
        ans=[0]
        n=len(s)
        @cache
        def solve(s):
            if len(s)==0:
                return 1
            first,second=0,0
            if s[0]!='0':
                first+=solve(s[1:])
            if 1<=int(s[0:2])<=26 and s[0]!='0' and len(s)>1:
                second+=solve(s[2:])
            return first+second
        return solve(s)
           
            
                
        