class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        i_did_get = False
        result = min(nums) 
        if result < 0:
            while  not i_did_get:
                curr = result
                for num in nums:
                    flag = True
                    curr += num
                    if curr < 1:
                        flag = False
                        break
                if not flag:
                    result += 1
                else:
                    if result < 1:
                        return 1
                    return result
        else:
            return 1