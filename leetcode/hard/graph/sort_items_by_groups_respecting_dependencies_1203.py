import collections
from typing import List


class Solution:
    @staticmethod
    def sortItems(n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topoSort(nodes, graph, in_degree):
            queue = collections.deque([node for node in nodes if node not in in_degree])

            ans = []

            while queue:
                cur_node = queue.popleft()
                ans.append(cur_node)

                for neighbor in graph[cur_node]:
                    in_degree[neighbor] -= 1

                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            return ans

        group_items = collections.defaultdict(list)
        groupId = m
        for i in range(n):
            if group[i] == -1:
                group[i] = groupId
                groupId += 1

            group_items[group[i]].append(i)

        item_graph = collections.defaultdict(list)
        item_indegree = collections.defaultdict(int)

        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] == group[v]:
                    item_graph[u].append(v)
                    item_indegree[v] += 1

        sorted_group_items = {}

        for groupId in group_items:
            sorted_items = topoSort(group_items[groupId], item_graph, item_indegree)

            if len(sorted_items) != len(group_items[groupId]):
                return []

            sorted_group_items[groupId] = sorted_items

        group_graph = collections.defaultdict(list)
        group_indegree = collections.defaultdict(int)

        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1

        groups = set(group)

        sorted_groups = topoSort(groups, group_graph, group_indegree)

        if len(groups) != len(sorted_groups):
            return []

        ans = []

        for groupId in sorted_groups:
            ans.extend(sorted_group_items[groupId])

        return ans


if __name__ == "__main__":
    print(
        Solution.sortItems(
            n=8, m=2, group=[-1, -1, 1, 0, 0, 1, 0, -1], beforeItems=[[], [6], [5], [6], [3, 6], [], [], []]
        )
    )
