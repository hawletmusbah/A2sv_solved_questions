from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # n = len(nums)
        # i = 0 
        # j = k
        # arr = []
        # while j < n+1:
        #     ranges = nums[i:j]
            
        #     maxi = max(ranges)
        #     # print(maxi)
        #     arr.append(maxi)
        #     j+=1
        #     i+=1
        # return arr
       


        dq = deque() # Stores indices
        res = []
        
        for i in range(len(nums)):
            # 1. Remove smaller numbers from the back (they can't be the max)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
                
            # 2. Add current index to the back
            dq.append(i)
            
            # 3. Remove the front index if it's out of the window range
            if dq[0] == i - k:
                dq.popleft()
                
            # 4. If we have a full window, the front of dq is the max
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res