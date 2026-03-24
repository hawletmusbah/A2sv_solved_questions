class Solution:
    def countGoodNumbers(self, n: int) -> int:

        # if n == 1:
        #     return 5
        # else:
        #     res = self.countGoodNumbers(n-1)
        #     if n % 2 == 0:
        #         return res *4 % (10**9 + 7)
        #     else:
        #         return res*5 % (10**9 + 7)
        

        
        MOD = 10**9 + 7

        even_pos = (n + 1) // 2
        odd_pos = n // 2
        
        first_part = pow(5, even_pos, MOD)
        second_part = pow(4, odd_pos, MOD)
        
        return (first_part * second_part) % MOD