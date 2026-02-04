N, M = map(int, input().split())

mat_a = [list(map(int, input().split())) for _ in range(N)]
mat_b = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(mat_a[i][j] + mat_b[i][j], end=' ')
    print()
