class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        # [0,1,2,3,4]
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
                
        def union(x,y):
            rootx = find(x)
            rooty = find(y)

            if rootx == rooty:
                return
            parent[rooty] = rootx
        
        for edge in edges:
            union(edge[0],edge[1])

        num = 0
        for i,p in enumerate(parent):
            if i == p:
                num += 1
        return num