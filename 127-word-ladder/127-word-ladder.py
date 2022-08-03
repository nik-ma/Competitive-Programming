from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=deque()
        q.append(beginWord)
        vis=set()
        vis.add(beginWord)
        words=set(wordList)
        ans=1
        while q:
            for i in range(len(q)):
                pt=q.popleft()
                if pt==endWord:
                    return ans
                used=[]
                for i in range(len(pt)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = pt[:i] + c + pt[i+1:]
                        if next_word in words:
                            words.remove(next_word)
                            q.append(next_word)
            ans+=1
        return 0
            