from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if (n != len(edges) - 1):
        #     return False
        # adj = defaultdict(set)
        # for edge in edges:
        #     a = edge[0]
        #     b = edge[1]
        #     adj[a].add(b)
        p = list(range(n))
        def find(x):
            if (x != p[x]):
                p[x] = find(p[x])
            return p[x]
                
        for a,b in edges:
            pa, pb = find(a), find(b)
            if p[a] == p[b]:
                return False
            # merge the two sets
            p[pa] = pb
            n-=1
        return n == 1
        # now we have to check each node for if there is a cycle
        # best way of doing this is by having a visited set, and marking this as either 
        # we also have to check if its connected
