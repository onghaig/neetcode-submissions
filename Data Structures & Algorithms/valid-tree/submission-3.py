class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if (n != len(edges) + 1):
        #     return False
        adj = defaultdict(set)
        for edge in edges:
            a = edge[0]
            b = edge[1]
            adj[a].add(b)
            adj[b].add(a)
        # cycle detection using dfs
        visited = {}
        
        def dfs(node,parent):
            if (node in visited):
                if (visited[node] == -1):
                    return False
                return True
            visited[node] = -1
            for nei in adj[node]:
                if (nei == parent):
                    continue
                if (not dfs(nei,node)):
                    return False
            visited[node] = 1
            return True
        return dfs(0,-1) and len(visited) == n