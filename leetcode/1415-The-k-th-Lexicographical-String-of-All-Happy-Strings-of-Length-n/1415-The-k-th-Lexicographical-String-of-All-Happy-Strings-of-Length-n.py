class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        s = ["a","b","c"]

        def backtracking(curr_stri):
            #base case 
            if len(result) == k:
                return 
            if len(curr_stri) == n:
                result.append("".join(curr_stri))
                return


            for i in s:
                if not curr_stri or i != curr_stri[-1]: 
                    curr_stri.append(i)
            
                    backtracking(curr_stri)
                    curr_stri.pop()

            

        backtracking([])
        if len(result) < k:
            return ""
        return result[k-1]