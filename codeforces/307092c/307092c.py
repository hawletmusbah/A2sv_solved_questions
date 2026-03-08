from collections import Counter
n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
countera = Counter(a)
counterb =  Counter(b)
i = 0
j = 0
count = 0
while i < n and j < m:
    # print(count)
    # print(a[i])

    if a[i] == b[j]:
        # print(countera[a[i]])
        # print(countera[b[j]])
        count += (countera[a[i]] * counterb[b[j]])
        # print(count)
        i += countera[a[i]]
        j += counterb[b[j]]
        # print(count)

    else:
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
print(count)