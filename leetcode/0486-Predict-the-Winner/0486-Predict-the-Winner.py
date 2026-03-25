class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def get_score(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]
            
            # Standard backtracking choices
            res = max(nums[left] - get_score(left + 1, right), 
                      nums[right] - get_score(left, right - 1))
            
            memo[(left, right)] = res
            return res

        return get_score(0, len(nums) - 1) >= 0