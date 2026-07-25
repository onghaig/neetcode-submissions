from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites: [[a,b][a,b]]
        # each course' prerequisite is formatted into its row.
        # for one row, we have all the prerequisites in there.
        # finding if there is a cycle in the graph
                #  whats the best way of doing that?
                # repeatedly doing dfs and seeing if we reach a node we've visited?
        adj = defaultdict(set)
        
        for a,b in prerequisites:
            adj[a].add(b)
        print(adj.items())

        visited = {}
        def dfs(a):
            if (a in visited):
                if (visited[a] == 1):
                    return True
                elif (visited[a] == 0):
                    return False
            visited[a] = 0
            for nei in adj[a]:
                print("executing neighbor" + str(nei))
                if not dfs(nei):
                    return False
            visited[a] = 1
            return True
        
        # where 0 is currently visiting
        # where 1 is visited
        for a in range(numCourses):
            if not dfs(a):
                return False
        return True