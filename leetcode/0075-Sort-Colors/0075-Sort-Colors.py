class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)
        init = zero
        mid = zero + one
        last = zero + one + two
        
        for i in range(0,init):
            nums[i] = 0
        
        for j in range(init,mid):
            nums[j] = 1
        
        for k in range(mid,last):
            nums[k] = 2