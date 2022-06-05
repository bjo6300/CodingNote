graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
print(graph_list[1] )

from collections import deque

def BFS_with_adj_list(graph_list, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph_list[n] - set(visited)
            print(graph_list[n], set(visited))
    return visited
  
print(BFS_with_adj_list(graph_list, root_node))


# dfs = 큐를 스택으로 변경, popleft() -> pop()
def DFS_with_adj_list(graph_list, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph_list[n] - set(visited)
    return visited

print(BFS_with_adj_list(graph_list, root_node))