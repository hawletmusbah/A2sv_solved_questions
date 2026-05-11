class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest_string = -1
        self.res = set()
        self.dfs(s, 0, [], 0, 0)
        
        
        return list(self.res) if self.res else [""]

    def dfs(self, string, cur_idx, cur_res, l_count, r_count):
        
        if cur_idx >= len(string):
           
            if l_count == r_count:
                current_str = "".join(cur_res)
                
               
                if len(current_str) > self.longest_string:
                    self.longest_string = len(current_str)
                    self.res = {current_str}
               
                elif len(current_str) == self.longest_string:
                    self.res.add(current_str)
            return

        cur_char = string[cur_idx]

        if cur_char == "(":
            # Choice 1: Keep the '('
            cur_res.append(cur_char)
            self.dfs(string, cur_idx + 1, cur_res, l_count + 1, r_count)
            cur_res.pop() # Backtrack

            # Choice 2: Remove the '('
            self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)

        elif cur_char == ")":
            # Choice 1: Remove the ')'
            self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)

            # Choice 2: Keep the ')' (Only if it doesn't make the string invalid)
            if l_count > r_count:
                cur_res.append(cur_char)
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count + 1)
                cur_res.pop() # Backtrack

        else:
            # It's a letter (a, b, c...)
            cur_res.append(cur_char)
            self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)
            cur_res.pop() # Backtrack