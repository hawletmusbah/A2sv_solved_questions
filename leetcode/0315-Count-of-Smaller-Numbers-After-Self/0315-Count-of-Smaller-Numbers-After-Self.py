class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        counts = [0] * n
        # Store indices to keep track of original positions after sorting
        indices = list(range(n))
        
        def merge_sort(arr_indices):
            if len(arr_indices) <= 1:
                return arr_indices
            
            mid = len(arr_indices) // 2
            left = merge_sort(arr_indices[:mid])
            right = merge_sort(arr_indices[mid:])
            
            return merge(left, right)

        def merge(left, right):
            merged = []
            l_ptr = 0
            r_ptr = 0
            # This keeps track of how many elements from the right side 
            # are smaller than the current element from the left side
            right_smaller_count = 0
            
            while l_ptr < len(left) and r_ptr < len(right):
                # If the element in the right side is smaller
                if nums[right[r_ptr]] < nums[left[l_ptr]]:
                    merged.append(right[r_ptr])
                    right_smaller_count += 1
                    r_ptr += 1
                else:
                    # If the element in the left side is smaller or equal
                    # We add the total count of smaller elements found in the right so far
                    counts[left[l_ptr]] += right_smaller_count
                    merged.append(left[l_ptr])
                    l_ptr += 1
            
            # Cleanup remaining elements
            while l_ptr < len(left):
                counts[left[l_ptr]] += right_smaller_count
                merged.append(left[l_ptr])
                l_ptr += 1
                
            while r_ptr < len(right):
                merged.append(right[r_ptr])
                r_ptr += 1
                
            return merged

        merge_sort(indices)
        return counts