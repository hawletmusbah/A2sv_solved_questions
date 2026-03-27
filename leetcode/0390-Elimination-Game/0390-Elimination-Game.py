class Solution:
    def lastRemaining(self, n: int) -> int:
        # arr = [i for i in range(1,n+1)]
        # def helper(i,arr):
        #     # base case 
        #     if len(arr) == 1:
        #         return arr[0]

        #     # recursive case   
            
        #     arr.pop(i) 
        #     print(arr)
        #     print(i)
        #     if i == (len(arr) -  1):
        #         return helper(i-1,arr)
        #     else:
        #         return helper(i+1,arr)
        # return helper(0,arr)
      
        
        if n == 1:
            return 1
        
        return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))