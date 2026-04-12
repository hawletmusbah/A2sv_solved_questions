class Solution:
    def can_place(self , mid,position,m):
        pre_pos = position[0]
        placed = 1
        for i in range(1,len(position)):
            curr_pos = position[i]
            if curr_pos - pre_pos >= mid:
                placed +=1
                pre_pos = curr_pos
            if placed == m:
                return True
        return False
        
    def maxDistance(self, position: List[int], m: int) -> int:
        #high = int(position[-1] / (m - 1.0)) + 1
        position.sort()
        ans = 0
        low = 1
        high = int(position[-1] / (m - 1.0)) + 1
        while low <= high:
            mid = low + (high - low)//2
            if self.can_place(mid,position,m):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans