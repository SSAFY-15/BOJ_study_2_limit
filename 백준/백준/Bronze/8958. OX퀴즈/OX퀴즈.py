T = int(input())
for _ in range(T):
    check = input()
    result=0
    point=0
    for s in check:
        if s =='O':
            point+=1
            result += point
        elif s=='X':
            point=0
    print(result)