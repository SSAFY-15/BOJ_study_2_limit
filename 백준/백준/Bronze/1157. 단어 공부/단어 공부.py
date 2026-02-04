from collections import Counter

input_string = input().lower()
count = Counter(input_string)
result = [k for k, v in count.items() if v == max(count.values())]
print(result[0].upper()) if len(result) == 1 else print('?')
