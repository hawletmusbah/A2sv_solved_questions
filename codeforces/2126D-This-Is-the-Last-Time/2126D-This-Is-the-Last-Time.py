t = int(input())
for _ in range(t):
    n,k  = list(map(int, input().split()))
    # l,r,re  = list(map(int, input().split()))
    main_list = []
    for _ in range(n):
        ci = list(map(int, input().split()))
        main_list.append(ci)
       
    # print(main_list)
    main_list.sort()
    
    for i in range(n):
        l,r,real = main_list[i]
        if k >=l and k<= r:
           
            if k < real:
                k = real
 
 
   
    print(k)