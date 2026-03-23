class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1indx = {n:i for i,n in enumerate(nums1)}
        # print(nums1indx)
        result = [-1] * len(nums1)
        stack = []
         
        for curr in nums2:
            while stack and curr > stack[-1]:
                indx = nums1indx[stack[-1]]
                result[indx] = curr
                stack.pop()
            if curr  in  nums1:
                stack.append(curr)
        return result