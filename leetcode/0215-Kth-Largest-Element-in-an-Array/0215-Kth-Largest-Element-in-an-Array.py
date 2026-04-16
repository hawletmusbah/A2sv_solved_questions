class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # for i in range(k-1):
        #     maxi = max(nums)
        #     nums.remove(maxi)
        # return max(nums)
        nums.sort()
        n = len(nums)
        return nums[n -k]