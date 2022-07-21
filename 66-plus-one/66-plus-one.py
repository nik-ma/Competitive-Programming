class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        val=digits[-1]+1
        digits[-1]=val%10
        carry=val//10
        for i in range(len(digits)-2,-1,-1):
            val=digits[i]+carry
            digits[i]=val%10
            carry=val//10
        if carry!=0:
            digits.insert(0,carry)
        return digits
        
        