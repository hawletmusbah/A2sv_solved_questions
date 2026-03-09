n,s = list(map(int, input().split()))
nums = list(map(int, input().split()))
total = 0
count = 0
i = 0
j = 0

for j in range(n):
    total += nums[j]
    while total >= s:
        count +=  n-j
        total -= nums[i]
        i += 1
        
print(count)