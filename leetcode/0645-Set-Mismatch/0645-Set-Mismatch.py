class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''n = len(nums)
        nums.sort()
        new_list = []
        print(nums)
        for i in range(n):
            if nums[i] != i+1:
                new_list.extend([nums[i] , i+1])

        return new_list'''
        
        n = len(nums)
        new_list = [0] * n
        for i in range(n):
            curr = nums[i]
            if curr not in new_list:
                new_list[curr-1] = curr
            else:
                rep = curr
        # print(new_list) 
        # print(rep)
        miss = new_list.index(0) +1
        # print(miss)
        return [rep,miss]