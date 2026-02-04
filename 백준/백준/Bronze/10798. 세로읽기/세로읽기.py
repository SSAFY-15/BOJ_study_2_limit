mat = [list(input()) for _ in range(5)]
result = ''
max_size = max(list(map(len, mat)))
for _ in range(max_size):
    for l in mat:
        if len(l) > 0:
            result += l.pop(0)
print(result)
