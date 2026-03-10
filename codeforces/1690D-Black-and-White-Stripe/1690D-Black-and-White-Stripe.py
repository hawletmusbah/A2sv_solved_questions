from collections import defaultdict
t = int(input())
for _ in range(t):
    n,k = list(map(int, input().split()))
    stri = input()
    nums = [char for char in stri]
    dictt = defaultdict(int)
    for i in range(k):
        if nums[i] == "W":
            dictt["W"] += 1
        else :
            dictt["B"] += 1
    
    l = 0
    r = k-1
    count = dictt["W"]
    
    while r < n-1:
        dictt[nums[l]] -= 1
        l += 1
        r += 1
        dictt[nums[r]] += 1
        
        count = min(count,dictt["W"])
    print(count)