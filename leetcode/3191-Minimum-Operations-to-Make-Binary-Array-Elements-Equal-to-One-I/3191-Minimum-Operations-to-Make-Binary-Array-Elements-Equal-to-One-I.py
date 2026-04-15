class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i = 0
        count = 0
        while i < len(nums) - 2:
            if nums[i] == 0:
                for j in range(i,i +3):
                    if nums[j] == 0:
                        nums[j] = 1
                    else:
                        nums[j] = 0 
                i +=1
                count += 1
            else:
                i += 1
                
        print(nums)
        if nums == [1] * len(nums):
            return count
        else:
            return -1