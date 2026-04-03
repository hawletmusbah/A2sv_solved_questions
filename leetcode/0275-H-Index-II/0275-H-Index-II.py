class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def thelimit(citations,limit):
            count = 0
            for i in citations:
                if i >= limit:
                    count += 1
            return count



        l =0
        r = max(citations)
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if thelimit(citations,mid) >= mid:
                ans = mid
                l = mid + 1
            else: 
                r = mid - 1

        return ans