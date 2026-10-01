class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        def find(x):
            if x == parent[x]:
                return parent[x]
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootx = find(x)
            rooty = find(y)

            if rootx == rooty:
                return rootx
            
            parent[rooty] = rootx

        # find the first time when the entire graph is connected
        candidates = set()
        for ai, bi in edges:
            # are they already connected?
            rootai = find(ai)
            rootbi = find(bi)
            res = union(ai,bi)
            if rootai == res or rootbi == res:
                candidates.add((ai,bi))
        print(candidates)
        for i in range(len(edges)-1, -1 , -1):
            if tuple(edges[i]) in candidates:
                return edges[i]

        return False
        # an edge can be removed if  
