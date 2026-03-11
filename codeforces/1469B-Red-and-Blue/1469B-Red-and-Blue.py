t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    r_sum = []
    b_sum = []
    total = 0
    for i in r:
        total += i
        r_sum.append(total)
    # print(r_sum)

    total = 0
    for j in b:
        total += j
        b_sum.append(total)
    # print(b_sum)
    # print(max(b_sum))
    # print(max(r_sum))
    b_max = max(b_sum)
    r_max = max(r_sum) 
    if  b_max < 0:
        b_max = 0
    if r_max < 0:
        r_max = 0

    maximum  = r_max + b_max
    print(maximum)