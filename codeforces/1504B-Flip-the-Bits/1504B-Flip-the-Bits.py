t = int(input())
for _ in range(t):
    
    n = int(input())
    a = input()
    b = input()
    
    
    

    a += '0'
    b += '0'
    
    balance = 0
    for i in range(n):
        if a[i] == '1': 
            balance += 1
        else: 
            balance -= 1
        
    
        current_matches = (a[i] == b[i])
        next_matches = (a[i+1] == b[i+1])
        
        if current_matches != next_matches:
            
            if balance != 0:
                print("NO")
                break
    else:           
        print("YES")