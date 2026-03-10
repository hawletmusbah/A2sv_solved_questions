from collections import defaultdict
n,k = list(map(int, input().split()))
nums = list(map(int, input().split()))
total_c = defaultdict(int)
count = 0
l = 0
 
 
for r in range(n):
    total_c[nums[r]] += 1
    while len(total_c) > k :
        total_c[nums[l]] -= 1
        if total_c[nums[l]] == 0:
            del total_c[nums[l]] 
        l += 1
    count += (r - l + 1)
    
print(count)