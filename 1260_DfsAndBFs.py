from collections import deque

n, m, v = map(int, input().split())
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
dfs_ans = []
bfs_ans = []

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort()

def dfs(x):
  dfs_visited[x] = True
  dfs_ans.append(x)
  for nx in graph[x]:
    if not dfs_visited[nx]:
      dfs(nx)

que = deque([v])
bfs_visited[v] = True
while que:
  x = que.popleft()
  bfs_ans.append(x)
  for nx in graph[x]:
    if not bfs_visited[nx]:
      bfs_visited[nx] = True
      que.append(nx)
dfs(v)

print(' '.join(map(str, dfs_ans)))
print(' '.join(map(str, bfs_ans)))