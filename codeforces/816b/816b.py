MAX = 200000  # depends on constraints

n, k, q = map(int, input().split())

freq = [0] * (MAX + 2)

for _ in range(n):
    l, r = map(int, input().split())
    freq[l] += 1
    freq[r + 1] -= 1

# Prefix sum to get actual frequencies
for i in range(1, MAX + 1):
    freq[i] += freq[i - 1]

# Mark admissible temperatures
good = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    if freq[i] >= k:
        good[i] = 1

# Prefix sum of admissible
prefix = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    prefix[i] = prefix[i - 1] + good[i]

# Answer queries
for _ in range(q):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a - 1])