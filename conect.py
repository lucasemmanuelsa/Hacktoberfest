def dfs(x1, y1, n):
    if x1 >= n or y1 >= n:
        return
    if x1 < 0 or y1 < 0:
        return
    if mat[x1][y1] == 1:
        return
    mat[x1][y1] = 1
    reach.append((x1, y1))
    dfs(x1 + 1, y1, n)
    dfs(x1 - 1, y1, n)
    dfs(x1, y1 + 1, n)
    dfs(x1, y1 - 1, n)

n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

s = []
for _ in range(n):
    s.append(input())

mat = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        mat[i][j] = int(s[i][j])

reach = []
dfs(x1, y1, n)
src = reach

reach = []
dfs(x2, y2, n)
dest = reach

cost = 0
ans = float('inf')
for i in range(len(src)):
    for j in range(len(dest)):
        cost = (src[i][0] - dest[j][0]) ** 2
        cost += (src[i][1] - dest[j][1]) ** 2
        ans = min(ans, cost)

if len(src) == 0 or len(dest) == 0:
    ans = 0

print(ans)
