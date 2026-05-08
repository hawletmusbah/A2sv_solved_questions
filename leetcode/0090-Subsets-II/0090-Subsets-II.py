class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(index,path,nums):
            #base case
            if path[:] not in result:
                result.append(path[:])
                
            while index < len(nums):
                path.append(nums[index])
                backtrack(index + 1,path,nums)
                path.pop()
                index += 1
        
        backtrack(0,[],nums)
        return result