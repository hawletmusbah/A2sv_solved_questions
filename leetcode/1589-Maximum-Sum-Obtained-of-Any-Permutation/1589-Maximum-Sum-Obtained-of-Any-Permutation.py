class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        nums.sort(reverse = True)
        listt = [0] * (n + 1)
        # print(nums)
        for start ,end in requests:
            listt[start] += 1
            listt[end+1] -= 1
        current = 0
        freq = []
        for i in listt:
            current += i
            freq.append(current)
        # print(freq)
        count = 0
        freq.sort(reverse = True)
        for i,j in zip(freq , nums):
            if i ==0:
                break
            count += i * j
            
        
        MOD = 10**9 + 7
        result = count % MOD
        return result