class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # having the list
        nums = []
        for i in range(1,n+1):
            nums.append(i)
            
        
        
        def helper(i , k ,nums):

            # base case
            if len(nums) == 1:
                return nums[0]
            index_to_remove = (i + k - 1) % len(nums)

            nums.pop(index_to_remove) 
            return helper(index_to_remove,k,nums)
        return helper(0,k,nums)