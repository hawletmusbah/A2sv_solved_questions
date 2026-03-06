class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = 0
        f = 0
        
        count = defaultdict(int)
        res = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            

            while len(count) > k:
                count[nums[n]] -= 1
                if count[nums[n]] == 0:
                    count.pop(nums[n])
                n += 1
                f = n

            while count[nums[n]] > 1:
                count[nums[n]] -= 1
                n += 1

            if len(count) == k:
                    res += n - f +1
        return res