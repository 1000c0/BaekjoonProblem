import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    visited[x][y] = True

    for dx, dy in [(1,0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

t = int(input())
for _ in range(t):
    ans = 0
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]

    for _ in range(k):
        px, py = map(int, input().split())
        graph[px][py] = 1
    
    for x in range(m):
        for y in range(n):
            if graph[x][y] == 1 and not visited[x][y]:
                dfs(x, y)
                ans += 1
    print(ans)