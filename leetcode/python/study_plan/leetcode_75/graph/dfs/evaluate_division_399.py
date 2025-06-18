from collections import defaultdict, deque
from typing import List


class Solution:

    @staticmethod
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
            return -1

        return [bfs(q[0], q[1]) for q in queries]

    @staticmethod
    def calcEquationSecond(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[
        float]:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        graph = defaultdict(list)

        for i, (u, v) in enumerate(equations):
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))

        # Graph structure after population
        # graph = {
        #     "a": [("b", 2)],
        #     "b": [("a", 1 / 2)],
        # }

        ans = []

        for f, t in queries:
            stack = [(f, 1)]
            visited = {f}
            has_answer = False

            # (x, x) case, where x is not given in the equations
            if f == t:
                if f not in graph:
                    ans.append(-1)
                else:
                    # (a, a) case, where "a" is in the graph and its value should be 1 == a/a
                    ans.append(1)
            else:
                while stack:
                    node, value = stack.pop()

                    if node == t:
                        ans.append(value)
                        has_answer = True

                    for neighbor, factor in graph[node]:
                        if neighbor not in visited:
                            stack.append((neighbor, value * factor))
                            visited.add(neighbor)

                if not has_answer:
                    ans.append(-1)

        return ans

    @staticmethod
    def dfs(self, graph: dict, start):
        visited = set()  # Set to track visited nodes
        stack = [start]  # Stack to store nodes to visit

        while stack:
            node = stack.pop()  # Get the next node from the stack

            if node not in visited:
                print(node)  # Process the current node
                visited.add(node)  # Mark the node as visited

                # Add unvisited neighboring nodes to the stack
                stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)


if __name__ == "__main__":
    # graph = {
    #     'A': ['B', 'C'],
    #     'B': ['D', 'E'],
    #     'C': ['F'],
    #     'D': [],
    #     'E': ['F'],
    #     'F': []
    # }

    # start_node = 'A'

    # Solution.dfs(Solution, graph, start_node)

    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(Solution.calcEquation(self=Solution, equations=equations, values=values, queries=queries))
