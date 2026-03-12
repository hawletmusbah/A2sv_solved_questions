class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        rem = {0: -1}
        total = 0
        for i ,value in enumerate(nums):
            total += value
            if total % k not in rem:
                rem[total % k] = i
            elif i - rem[total % k] > 1:
                return True
        return False