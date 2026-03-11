t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 0:
        print(0)
        print()
        continue
            
    ans = []
        
    ans.append(a[0])
        
        
    for i in range(1, n - 1):
            
        if (a[i] - a[i-1]) * (a[i+1] - a[i]) < 0:
            ans.append(a[i])
        
        
    if n > 1:
        ans.append(a[n-1])
            
        
    print(len(ans))
    
    print(*(ans))