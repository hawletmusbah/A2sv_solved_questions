class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
       
        target = len(graph) - 1
        results = []
        
        def dfs(current_node, path):
            
            if current_node == target:
                results.append(list(path))
                return
            
            
            for neighbor in graph[current_node]:
                path.append(neighbor)  
                dfs(neighbor, path)    
                path.pop()            

        
        dfs(0, [0])
        return results