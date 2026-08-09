class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph={i:[] for i in range(n)}
        for n in edges:
            graph[n[0]].append(n[1])
            graph[n[1]].append(n[0])
        count=0
        ans=0
        visited=set()
        def dfs(root):
            visited.add(root)
            if not graph[root]:
                return
            for n in graph[root]:
                if n not in visited:
                    dfs(n)
            return
        for i in graph:
            if i not in visited:
                count+=1
                dfs(i)
        return count

        