N = int(input())

n_list = list(map(int, input().split()))

M = int(input())

m_list = list(map(int, input().split()))

n_set = set(n_list)
m_set = set(m_list)
com_set = m_set & n_set
count = []
for i in m_list:
    if i in com_set:
        count.append(1)
    else:
        count.append(0)
print(*count)

