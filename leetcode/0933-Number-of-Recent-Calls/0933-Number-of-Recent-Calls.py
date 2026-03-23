from collections import deque
class RecentCounter:


    def __init__(self):
        self.q = deque()



    def ping(self, t: int) -> int:
        flage = True
        self.q.append(t)
        while flage:
            if self.q[0] not in range(t - 3000 , t+1):
                self.q.popleft()
            else:
                break
        return len(self.q)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)