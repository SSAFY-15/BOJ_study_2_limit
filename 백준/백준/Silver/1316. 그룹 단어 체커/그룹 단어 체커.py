N = int(input())
count = 0
for _ in range(N):
    temp_arr = []
    input_str = input()
    last_str = input_str[0]
    group_str = True
    for s in input_str:
        if s in temp_arr:
            if last_str != s:
                group_str = False
                break
        else:
            temp_arr.append(s)
        last_str = s
    if group_str:
        count += 1

print(count)
