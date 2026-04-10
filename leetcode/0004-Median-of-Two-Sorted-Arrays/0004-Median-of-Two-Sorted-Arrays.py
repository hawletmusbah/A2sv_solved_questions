class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = 0
        right = 0
        ans = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                ans.append(nums1[0])
                nums1.remove(nums1[0])
            else:
                ans.append(nums2[0])
                nums2.remove(nums2[0])
        if nums1:
            ans.extend(nums1)
        if nums2:
            ans.extend(nums2)
        n = len(ans)
        if n % 2 == 0:
            return (ans[(n//2) - 1] + ans[(n//2)])/2
        else:
            return ans[(n+1)//2 -1]