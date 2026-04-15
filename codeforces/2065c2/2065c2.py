t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b.sort()
    flag = True

    def giveThenumber(b, pre, curr):
        ans = None
        l = 0
        r = m - 1
        while l <= r:
            mid = (l + r) // 2
            if b[mid] - curr >= pre:
                ans = b[mid]
                r = mid - 1
            else:
                l = mid + 1
        return ans

    # handle first element
    a[0] = min(a[0], b[0] - a[0])

    for i in range(1, n):
        pre = a[i-1]
        curr = a[i]

        bj = giveThenumber(b, pre, curr)

        candidates = []

        # option 1: keep curr
        if curr >= pre:
            candidates.append(curr)

        # option 2: transform
        if bj is not None:
            val = bj - curr
            if val >= pre:
                candidates.append(val)

        # no valid option
        if not candidates:
            print("NO")
            flag = False
            break

        # choose smallest valid
        a[i] = min(candidates)

    if flag:
        print("YES")