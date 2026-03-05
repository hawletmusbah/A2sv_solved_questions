t =  int(input())
for _ in range(t):
    n  =  int(input())
    a = list(map(int, input().split())) 
    b = list(map(int, input().split()))
    
    listt = []
    for j in range(n):
            if a[j] > b[j]:
                a[j] , b[j] = b[j] , a[j]
                
                listt.append((3,j+1))
    for i in range(n):
        for j in range(1,n):
            if a[j] < a[j-1]:
                a[j] , a[j-1] = a[j-1] , a[j]
                
                listt.append((1,j))
        
 
    for i in range(n):
        for j in range(1,n):
            if b[j] < b[j-1]:
                b[j] , b[j-1] = b[j-1] , b[j]
                
                listt.append((2,j))
    
 
   
   
    print(len(listt))
    for x,y in listt:
        print(f"{x} {y}")