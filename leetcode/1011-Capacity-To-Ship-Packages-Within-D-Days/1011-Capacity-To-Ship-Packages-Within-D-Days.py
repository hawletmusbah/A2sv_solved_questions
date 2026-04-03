class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def howmanydays (weights,limit):
            summ = 0
            count = 1
            for i in weights:
                if summ + i > limit:
                    count += 1
                    summ = 0
                    summ += i
                else:
                    summ += i
            return count
        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = (l+r) // 2
            if howmanydays(weights,mid) <= days:
                r =  mid 
            else:
                l = mid + 1
        return r