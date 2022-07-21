class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0

        for n1 in num1:
            temp = 0
            for n2 in num2:
                temp = temp * 10 + int(n1) * int(n2)
            ans = ans * 10 + temp

        return str(ans)
            
        