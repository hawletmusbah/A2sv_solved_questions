class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n+1)
        for i in citations:
            count[min(i,n)] += 1
        h = n
        total = count[n]
        
        while total < h:
            
            h -= 1
            total += count[h] 
        return h