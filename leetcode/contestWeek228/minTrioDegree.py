class Solution(object):
    def minTrioDegree(self, n, edges):
        graph = defaultdict(set)
        for u,v  in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        ans = INF = float('inf')
        for v, w in edges:
            for u in graph[v] & graph[w]:
                deg = len(graph[u]) + len(graph[v]) + len(graph[w])
                deg -= 6
                if deg < ans: ans = deg
        return ans if ans < INF else -1