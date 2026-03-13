class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def the_goal(x):
            if x < 0 :
                return 0
            l = 0
            summ = 0
            res  = 0
            for r in range(len(nums)):
                summ += nums[r]
                while summ > x:
                    summ -= nums[l]
                    l += 1
                res += (r - l + 1)
            return res

        return the_goal(goal) - the_goal(goal -1 )