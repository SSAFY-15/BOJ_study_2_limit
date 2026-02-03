N = int(input())

num_list = list(map(int, input().split()))
max_val = max(num_list)
new_list = list(map(lambda x: x / max_val * 100, num_list))
print(sum(new_list)/N)
