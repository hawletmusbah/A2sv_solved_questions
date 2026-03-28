class Solution:
    def permute(self, nums):
        ans = []    # To store all final permutations
        ds = []     # Data structure to store the current permutation
        # freq array to keep track of which indices are already used
        freq = [False] * len(nums)
        
        self.recurPermute(nums, ds, ans, freq)
        return ans

    def recurPermute(self, nums, ds, ans, freq):
        # Base Case: If the current list size equals the input array size,
        # we have found a valid permutation.
        if len(ds) == len(nums):
            # We must append a COPY of ds, because ds is modified during backtracking
            ans.append(list(ds))
            return

        for i in range(len(nums)):
            # If the element at index i has not been used yet
            if not freq[i]:
                # 1. Mark as used
                freq[i] = True
                # 2. Add to current permutation
                ds.append(nums[i])
                
                # 3. Recurse to pick the next element
                self.recurPermute(nums, ds, ans, freq)
                
                # 4. Backtrack: remove last element and mark index as unused
                ds.pop()
                freq[i] = False