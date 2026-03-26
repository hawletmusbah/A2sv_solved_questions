class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n  = len(nums)
        result ,sol = [] , []
        def backtracking(start):
            if start == n:
                result.append(sol[:])
                return
            backtracking(start + 1)

            sol.append(nums[start])
            backtracking(start + 1)
            sol.pop()

        backtracking(0)
        return result