class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = float("-inf")
        cu_sum = 0
        for i in range(len(nums)):
            cu_sum += nums[i]
            if cu_sum < 0:
                summ = max(summ,cu_sum)
                cu_sum = 0
            else:
                summ = max(summ,cu_sum)

        return summ