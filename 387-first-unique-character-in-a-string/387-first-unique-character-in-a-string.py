class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicti=defaultdict(int)
        for i in s:
            dicti[i]+=1
        for i in range(len(s)):
            if dicti[s[i]]==1:
                return i
        return -1
        