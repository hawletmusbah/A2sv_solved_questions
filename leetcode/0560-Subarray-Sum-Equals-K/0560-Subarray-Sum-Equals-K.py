class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        t_sum = 0
        dictt = {0:1}
        res = 0
        for i in nums:
            t_sum += i
            diff = t_sum - k
            res += dictt.get(diff, 0)
            dictt[t_sum] = 1 + dictt.get(t_sum, 0)
        return res