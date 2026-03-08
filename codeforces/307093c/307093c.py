n,s = list(map(int, input().split()))
nums = list(map(int, input().split()))
total = 0
count = 0
i = 0
j = 0

while j < n:
    total += nums[j]
    while total > s and i <= j:
        total -= nums[i]
        i += 1
    count += (j - i + 1)
    
    j += 1
print(count)