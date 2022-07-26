from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dicti=defaultdict(lambda :[0,0])
        for i in matches:
            dicti[i[0]][0]+=1
            dicti[i[1]][1]+=1
        winners=[]
        losers=[]
        for i in dicti:
            if dicti[i][1]==0:
                winners.append(i)
            elif dicti[i][1]==1:
                losers.append(i)
        return [sorted(winners),sorted(losers)]
            
        