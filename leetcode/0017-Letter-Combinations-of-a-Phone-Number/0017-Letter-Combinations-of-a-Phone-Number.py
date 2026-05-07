class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        
        my_dict = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        if not digits:
            return []
        else:
            

            def backtracking(path,index):
                
                #base case 
                if len(path) == len(digits):
                    result.append("".join(path))
                    return

                c_digits = digits[index]
                letters = my_dict[c_digits]
                for letter in letters:
                    path.append(letter)
                    backtracking(path,index + 1)
                    path.pop()
            backtracking([],0)
            return result