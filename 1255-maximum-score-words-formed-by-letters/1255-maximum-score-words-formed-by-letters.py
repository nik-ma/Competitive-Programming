class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        score = [sum(score[ord(c)-ord('a')] for c in w) for w in words]
        words = list(map(Counter, words))
        
        res = [0]
        def dfs(i, cur, c):
            res[0] = max(res[0], cur)
            for j, w in enumerate(words[i:], i):
                if not w - c:
                    dfs(j+1, cur + score[j], c - w)
        dfs(0, 0, Counter(letters))
        return res[0]