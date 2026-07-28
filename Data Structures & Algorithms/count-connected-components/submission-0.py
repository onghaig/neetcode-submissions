from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # first, lets make it so that the edges form an adjacency table
        adjmat = defaultdict(set)
        for edge in edges:
            a,b = edge
            adjmat[a].add(b)
            adjmat[b].add(a)
        # now we have adjmat, where each node is linked to the set of its neighbors.
        # Recall the union-find algorithm
            #  we have a find function that helps us find the root of the set
        parent= [i for i in range(n)]
        # each node has its own position in the array.

        def find(x):
            if (parent[x] == x):
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootx = find(x)
            rooty = find(y)

            if (rootx == rooty):
                # already the same
                return
            
            parent[rooty] = rootx

        for node in range(n):
            for nei in adjmat[node]:
                union(node,nei)
        print(parent)
        # now we just need to know how many different sets there are
        count = 0
        for i,p in enumerate(parent):
            if i == p: 
                count+=1
        return count
