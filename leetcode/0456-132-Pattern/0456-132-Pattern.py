class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # have = 0
        # stack = []
        # for num in nums:
        #     if not stack:
        #         stack.append(num)
        #     elif num > stack[-1]:
        #         stack.append(num)
        #         have = nums.index(num)
        #     elif num < stack[-1] and len(stack) > 1 and (stack[-1]-num) < (stack[-1]-nums[ha-1]):
        #         return True
        #     else:
        #         stack.pop()
        #         stack.append(num)
        #     ha = max(have,nums.index(num))
        #     print(have)

        # return False

        stack = [] #increasing
        curmin = nums[0]

        for i in nums[1:]:
            while stack and i >= stack[-1][0]:
                stack.pop()
            if stack and i > stack[-1][1]:
                return True
            stack.append([i , curmin])
            curmin = min(curmin,i)
        return False