from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deq = deque()    # inreases      
        max_deq = deque()   # decreases
        res = 0
        l = 0

        for r in range(len(nums)):
            while min_deq and min_deq[-1] > nums[r]:
                min_deq.pop()
            while max_deq and max_deq[-1] < nums[r]:
                max_deq.pop()
            
            min_deq.append(nums[r])
            max_deq.append(nums[r])

            while max_deq[0] - min_deq[0] > limit:
                if nums[l] == max_deq[0]:
                    max_deq.popleft()
                if nums[l] == min_deq[0]:
                    min_deq.popleft()
                l += 1
            res = max(res , r - l +1)
        return res