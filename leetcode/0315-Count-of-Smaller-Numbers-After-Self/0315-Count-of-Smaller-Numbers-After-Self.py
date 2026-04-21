class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # counts = [0]*len(nums)
        # for i in range(len(nums)):
        #     number  = nums[i]
        #     for j in range(i+1,len(nums)):
        #         if nums[j] < number:
        #             counts[i] += 1
        # return counts \
        # indexed_nums = list(enumerate(nums))
        # def merge_sort(arr):
        #     mid = len(arr)//2
        #     left = merge(arr[:mid])
        #     right = merge(arr[mid:])


        # n = len(nums) 
        # count = [0]*len(nums)
        # def merge(left , right):
        #     i = 0
        #     j = 0 
        #     new_list = []
        #     while i < len(left) and j < len(right):
        #         if left[i] < right[j]:
        #             new_list.append(left[i][0])
        #             count[left[1]] += j
        #             i += 1
        #         else:
        #             new_list.append(right[j][0])
        #             j += 1
        n = len(nums)
        self.count = [0] * n
        
        indexed_nums = list(enumerate(nums)) 
        indexed_nums = [(nums[i], i) for i in range(n)]
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            i = 0
            j = 0 
            new_list = []
            
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    self.count[left[i][1]] += j
                    new_list.append(left[i])
                    i += 1
                else:
                    new_list.append(right[j])
                    j += 1
            while i < len(left):
                self.count[left[i][1]] += j
                new_list.append(left[i])
                i += 1
            
            
            while j < len(right):
                new_list.append(right[j])
                j += 1
                
            return new_list

        merge_sort(indexed_nums)
        return self.count