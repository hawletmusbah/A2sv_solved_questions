class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = 1
        high = sum(candies) // k
        
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            
            total_children_covered = 0
            for pile in candies:
                total_children_covered += pile // mid
            
       
            if total_children_covered >= k:
                ans = mid   
                low = mid + 1
            else:
                high = mid - 1 
                
        return ans