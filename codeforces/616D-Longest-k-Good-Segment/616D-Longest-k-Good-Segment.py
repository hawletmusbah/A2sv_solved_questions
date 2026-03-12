from collections import defaultdict
n,k = list(map(int, input().split()))
nums = list(map(int, input().split()))
l = 0
r = 0
l_p = 1
r_p = 1
dictt =defaultdict(int)
length = 0
while r < n and l < n:
    dictt[nums[r]] += 1
    if len(dictt) <= k:
        if r-l + 1 > length:
            length = r-l + 1 
            l_p = l + 1
            r_p = r + 1
        r+= 1
    else:
        dictt[nums[l]] -= 1
        if dictt[nums[l]] == 0:
            del dictt[nums[l]]
        l += 1
        r += 1
print(l_p ,r_p)