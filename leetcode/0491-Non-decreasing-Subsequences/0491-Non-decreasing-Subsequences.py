class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        
            
        def backtracking(index,path,nums):
            # base case 
            if len(path) >= 2:
                result.append(path[:])
                
            used = set()
            while index < len(nums):
                if nums[index] in used:
                    index += 1
                    continue

                if not path or nums[index] >= path[-1]:
                    used.add(nums[index])
                    
                    path.append(nums[index])
                    backtracking(index + 1,path,nums)
                    path.pop()
                index += 1
        backtracking(0,[],nums)
        return result