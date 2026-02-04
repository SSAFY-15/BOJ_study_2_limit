T = int(input())

for _ in range(T):
    number, input_string = input().split()
    result = ''
    for s in input_string:
        result += s * int(number)
    print(result)
