class Solution:
    def distributeCookies(self, cookies, k):
        print(cookies)
        self.ans = float('inf') 
        sums = [0] * k


        def backtrack(index):
            if index == len(cookies):
                self.ans = min(self.ans, max(sums))
                return 

            for i in range(k):
                if (sums[i] + cookies[index]) >= self.ans:
                    continue
                else:
                    sums[i] += cookies[index]
                    backtrack(index + 1)
                    sums[i] -= cookies[index]
            
       
        backtrack(0)
        
      
        return self.ans