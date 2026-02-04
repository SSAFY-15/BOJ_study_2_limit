from collections import defaultdict

result = 1
for _ in range(3):
    result = result * int(input())

result = str(result)

count = defaultdict(int)

for s in result:
    count[int(s)] += 1

for i in range(10):
    print(count.get(i, 0))
