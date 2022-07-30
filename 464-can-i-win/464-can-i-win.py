class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal == 0:
            return True
        self.max = maxChoosableInteger
        self.d = {}
        
        if desiredTotal > maxChoosableInteger * (maxChoosableInteger+1) // 2:
            return False
        
        return self.recursion(2**maxChoosableInteger-1, desiredTotal)
        
    
    def recursion(self, mask, total):  #bit 'set' means still not chosen 
        
        if mask >= 2**(total-1):
            return True
        if mask in self.d:
            return self.d[mask]
        
        for i in range(self.max):
            if mask & (1<<i):  #if the ith bit is set
                newmask = mask & ~(1<<i)  #unset the ith bit
                if self.recursion(newmask, total-i-1) == False:
                    self.d[mask] = True
                    return True
        self.d[mask] = False
        return False