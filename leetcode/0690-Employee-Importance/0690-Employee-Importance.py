from collections import deque

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {emp.id: emp for emp in employees}
        total_importance = 0
        queue = deque([id])
        
        while queue:
            curr_id = queue.popleft()
            curr_emp = emp_map[curr_id]
            total_importance += curr_emp.importance
            
            # Add all subordinates to the queue to process them next
            for sub_id in curr_emp.subordinates:
                queue.append(sub_id)
                
        return total_importance