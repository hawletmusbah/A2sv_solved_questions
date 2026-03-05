n,k  = list(map(int, input().split()))
nums = list(map(int, input().split()))
new_list = []
cut = k -1
for i in range(n-1):
    new_list.append(nums[i+1] - nums[i])
# print(new_list)
new_list.sort(reverse=True)
sol = nums[n-1] - nums[0]
for j in range(cut):
    sol -= new_list[j]
print(sol)